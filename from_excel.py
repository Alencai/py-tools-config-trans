#!/usr/bin/python
# -*-coding:utf-8-*-
import os, glob, re, io
import xml.dom.minidom
import sys, json
import xlrd
from sys import version_info

is_py2 = False

if version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    is_py2 = True
else:
    import importlib 
    importlib.reload(sys)

#--------------------------------------------------

in_excels = "."
in_config = None
out_files = "."
out_end = ""
str_dot = '"'
str_newidn = "    "
str_newline = "\n"

#--------------------------------------------------

strIsDouble = re.compile('^-?\d*\.?\d*$')
strIsInt = re.compile('^(-?\d*)\.?0?$')  # 匹配.0结尾的数字，方便去掉.0

def parseXmlSetting(parent):
    result = []
    tables = parent.getElementsByTagName('table')
    if tables is not None and len(tables) > 0:
        for table in tables:
            item = {}
            item['path'] = table.getAttribute('path')
            item['sheetname'] = table.getAttribute('sheetname')
            item['jsonname'] = table.getAttribute('jsonname')
            item['fields'] = []
            fields = table.getElementsByTagName('field')
            if fields is not None and len(fields) > 0:
                for field in fields:
                    sub_item = {}
                    sub_item['name'] = field.getAttribute('name')
                    sub_item['map'] = field.getAttribute('map')
                    sub_item['type'] = field.getAttribute('type')
                    item['fields'].append(sub_item)
            result.append(item)
    return result

def dealWithExcel(data, fields, sheetName, jsonname):
    print('dealing: ', jsonname)
    str_result = '[' + str_newline
    table = data.sheet_by_name(sheetName)
    if table is None:
        print('error: can\'t find sheetname: ', sheetName)
        return
    ncols = table.ncols
    nrows = table.nrows - 3
    for field in fields:  
        isError = True
        field_map = field['map']
        field_type = field['type']
        for col in range(ncols):
            col_map = table.cell(1, col).value
            col_type = table.cell(0, col).value
            if field_map == col_map and field_type == col_type:
                field['col'] = col
                isError = False
                break
        if isError:
            print('error: field map and type: ', field_map, field_type)
            return
    not_first = False
    for row in range(nrows):
        sub_not_first = False
        str_result += (not_first and ("," + str_newline) or '')
        str_result += '{' + str_newline
        for field in fields:  
            col = field['col']
            field_name = field['name']
            field_type = field['type']
            str_result += (sub_not_first and ("," + str_newline) or '')
            field_item = table.cell(3 + row, col)
            # field_item.ctype: (0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error)
            value = str(field_item.value)
            if is_py2:
                value = value.encode('utf-8')
            if field_type == 'string':
                # 建议在excel中，单元格为数字的字符串前加单引号（'）     
                # 即可强制字符串格式存储，在此处读取时就不会变成number类型    
                if field_item.ctype == 2:
                    reInt = strIsInt.match(value)
                    if not (reInt is None):
                        value = reInt.group(1)
                str_result += str_newidn + str_dot + field_name + str_dot + ':"' + value + '"'
            elif field_type == 'double':
                if strIsDouble.match(value) is None:
                    print('error: double value: ', value)
                    return
                if len(value) == 0:
                    value = "0"
                str_result += str_newidn + str_dot + field_name + str_dot + ':' + value
            elif field_type == 'int':
                reInt = strIsInt.match(value)
                if reInt is None:
                    print('error: int value: ', value)
                    return
                value = reInt.group(1)
                if len(value) == 0:
                    value = "0"
                str_result += str_newidn + str_dot + field_name + str_dot + ':' + value
            else:
                print('error: unknow type: ', field_type, value)
                return
            sub_not_first = True
        str_result += str_newline + '}' + str_newline
        not_first = True
    str_result += ']' + str_newline
    out_path = os.path.join(out_files, jsonname + '.' + out_end)
    if is_py2:
        out_path = out_path.encode('GBK')
    print('write: ', out_path)
    with open(out_path, 'w') as file:
        file.write(str_result)

def write():
    # 先删除输出目录下的旧文件（防止配置删除后，这个目录下的旧文件依然存在）
    strIsJson = re.compile('^.*\.' + out_end + '$')
    out_path = out_files
    if is_py2:
        out_path = out_path.encode('GBK')
    for root, dirs, files in os.walk(out_path): 
        for file in files:
            if strIsJson.match(file) is not None:
                print('remove: ', file)
                os.remove(os.path.join(root, file)) 
        break
    # 然后开始转化excel
    if in_config is not None:
        in_path = in_config
        if is_py2:
            in_path = in_path.encode('GBK')
        dom = xml.dom.minidom.parse(in_path)
        arrSettings = parseXmlSetting(dom.documentElement)
        for setting in arrSettings:
            path = os.path.join(in_excels, setting['path'])
            if is_py2:
                path = path.encode('GBK')
            data = xlrd.open_workbook(path)
            if data is None:
                print('error: can\'t find path: ', path)
                return
            dealWithExcel(data, setting['fields'], setting['sheetname'], setting['jsonname'])

