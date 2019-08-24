#!/usr/bin/python
# -*-coding:utf-8-*-

import xml.dom.minidom
import xlrd
import json
import io

# -------------------------------------------------

from _base._str import *
from _base._re import *
from _base._file import *

# -------------------------------------------------

KEY_PATH = 'path'
KEY_SHEETNAME = 'sheetname'
KEY_JSONNAME = 'jsonname'
KEY_FIELDS = 'fields'
KEY_FIELD_NAME = 'name'
KEY_FIELD_TYPE = 'type'
KEY_FIELD_MAP = 'map'
KEY_FIELD_COL = 'col'

# -------------------------------------------------

class MyParserExcel:
    __settings = []

    # 根据配置，匹配表上的字段是否缺失，或者类型错误
    def _matchSettingFields(self, table, fields):
        ncols = table.ncols
        for field in fields:
            field_type = field[KEY_FIELD_TYPE]
            field_map = field[KEY_FIELD_MAP]
            field[KEY_FIELD_COL] = None
            for col in range(ncols):
                col_type = table.cell(0, col).value
                col_map = table.cell(1, col).value
                if field_map == col_map and field_type == col_type:
                    field[KEY_FIELD_COL] = col
                    break
            assert (field[KEY_FIELD_COL] != None), ('Error: field.map or field.type can not find: %s %s' % (field_map, field_type))

    # 根据配置的type，获取excel单元格value
    def _getExcelFieldValue(self, table_item, field_type):
        # table_item.ctype: (0 empty, 1 string, 2 number, 3 date, 4 boolean, 5 error)
        if 0 <= table_item.ctype and table_item.ctype <= 2:
            value = enUTF8(str(table_item.value))
            if field_type == 'string':
                # 建议在excel中，单元格为数字的字符串前加单引号（'）     
                # 即可强制字符串格式存储，在此处读取时就不会变成number类型    
                if table_item.ctype == 2:
                    ret = getExcelInt(value) # 去除excel中int类型的后缀“.0”
                    assert ret, ('Error: int value %s %s' % (field_type, value))
                    return ret 
                return value
            if field_type == 'double':
                ret = getExcelDouble(value)
                assert ret, ('Error: double value %s %s' % (field_type, value))
                return float(ret)
            if field_type == 'int':
                ret = getExcelInt(value)
                assert ret, ('Error: int value %s %s' % (field_type, value))
                return int(ret)
        assert False, ('Error: unknow type: %s %s' % (field_type, value))
        return value
    
    def _getJsonExcel(self, table, fields):
        ret_json = []
        for row in range(table.nrows - 3):
            row_json = {}
            for field in fields:  
                table_item = table.cell(3 + row, field[KEY_FIELD_COL])
                table_value = self._getExcelFieldValue(table_item, field[KEY_FIELD_TYPE])
                row_json[field[KEY_FIELD_NAME]] = table_value
            ret_json.append(row_json)
        return ret_json

    #-----------------------------------------------------------------------------------

    # 返回json字符串
    def _exportJsonStr(self, table, fields):
        ret_json = self._getJsonExcel(table, fields)
        ret_str = json.dumps(ret_json, sort_keys = True, indent = 4) # encoding = 'utf-8'
        return deUnicode(ret_str)
    
    #-----------------------------------------------------------------------------------
    
    # 读取excel字段配置表
    # <table path="excel1.xlsx" sheetname="Sheet1" jsonname="excel1">
    # 	<field name="id" map="id" type="int"/>
    # 	<field name="name" map="name" type="string"/>
    # </table>
    def parseSettingXml(self, file_name):
        self.__settings = []
        xml_dom = xml.dom.minidom.parse(file_name)
        assert xml_dom, ('error: can not find file: %s' % (file_name))
        ele_root = xml_dom.documentElement
        ele_sets = ele_root.getElementsByTagName('table')
        for setting in ele_sets:
            item = {}
            item[KEY_PATH] = setting.getAttribute('path')
            item[KEY_SHEETNAME] = setting.getAttribute('sheetname')
            item[KEY_JSONNAME] = setting.getAttribute('jsonname')
            item[KEY_FIELDS] = []
            fields = setting.getElementsByTagName('field')
            for field in fields:
                sub_item = {}
                sub_item[KEY_FIELD_NAME] = field.getAttribute('name')
                sub_item[KEY_FIELD_TYPE] = field.getAttribute('type')
                sub_item[KEY_FIELD_MAP] = field.getAttribute('map')
                item[KEY_FIELDS].append(sub_item)
            self.__settings.append(item)

    # 导出配置到文件
    def exportFiles(self, in_dir, out_dir):
        reloadSys()
        createDir(out_dir)
        for setting in self.__settings:
            file_name = os.path.join(in_dir, setting[KEY_PATH])
            sheet_name = setting[KEY_SHEETNAME]
            json_file = setting[KEY_JSONNAME]
            fields = setting[KEY_FIELDS]
            data = xlrd.open_workbook(file_name)
            assert data, ('error: can not find file: %s' % (file_name))
            table = data.sheet_by_name(sheet_name)
            assert table, ('Error: can not find sheetname: %s' % (sheet_name))
            self._matchSettingFields(table, fields)
            if json_file:  # 导出json
                write_path = os.path.join(out_dir, json_file + '.json')
                json_str = self._exportJsonStr(table, fields)
                writeFile(json_str, write_path)


