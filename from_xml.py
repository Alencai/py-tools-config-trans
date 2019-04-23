#!/usr/bin/python
# -*-coding:utf-8-*-
import os, glob, re, io
import xml.dom.minidom
import sys, json
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

in_files = "."
in_file_end = "json"
in_xmls = "."
out_pre = ""
out_end = ""
out_file = ""
str_dot = '"'
str_newidn = "    "
str_newline = "\n"

#--------------------------------------------------

xmlNameRe = re.compile('(.+)\.xml')
strIsNumber = re.compile('^-?\d*\.?\d*$')


def parseXmlSetNodes(parent):
    ret = {}
    childs = parent.childNodes
    for child in childs:
        if child.nodeType == 1:
            data = parseXmlSetNodes(child)
            json.dumps(data)
            key = child.getAttribute('dictionary')
            if key is not None and key is not "":
                data['_type'] = 2
                data['_key'] = key
            elif child.getAttribute('array') == "true":
                data['_type'] = 3
            else:
                data['_type'] = 1
            ret[child.nodeName] = data
    return ret

def parseXmlSetting(parent):
    elements = parent.getElementsByTagName('__setting')
    if elements is not None and len(elements) > 0:
        return parseXmlSetNodes(elements[0])
    return {}

def parseXmlDict(dictSetting, parent, name, idn):
    str_result = ''
    not_first = False
    key = dictSetting['_key']
    str_result += idn + str_dot + name + str_dot + ':{' + str_newline
    # childs = parent.getElementsByTagName(name)
    childs = parent.childNodes
    for child in childs:
        if child.nodeType == 1 and child.nodeName == name and child.hasAttribute(key):
            str_result += (not_first and ("," + str_newline) or '')
            str_result += idn + str_newidn + str_dot + child.getAttribute(key) + str_dot + ':'
            str_result += parseXmlNode(dictSetting, child, idn + str_newidn)
            not_first = True
    str_result += (not_first and str_newline or '') + idn + '}'
    return str_result

def parseXmlArray(dictSetting, parent, name, idn):
    str_result = ''
    not_first = False
    str_result += idn + str_dot + name + str_dot + ':[' + str_newline
    # childs = parent.getElementsByTagName(name)
    childs = parent.childNodes
    for child in childs:
        if child.nodeType == 1 and child.nodeName == name:
            str_result += (not_first and ("," + str_newline) or '')
            str_result += idn + str_newidn
            str_result += parseXmlNode(dictSetting, child, idn + str_newidn)
            not_first = True
    str_result += (not_first and str_newline or '') + idn + ']'
    return str_result

def parseXmlNode(dictSetting, parent, idn):
    dictHashHdl = {}
    not_first = False
    str_result = '{' + str_newline
    attrs = parent.attributes
    for key in attrs.keys():
        value = parent.getAttribute(key)
        if strIsNumber.match(value) is None:
            value = '"' + value + '"'
        str_result += (not_first and ("," + str_newline) or '')
        str_result += idn + str_newidn + str_dot + key + str_dot + ':' + value
        not_first = True
    childs = parent.childNodes
    for child in childs:
        if child.nodeType == 1:
            if child.nodeName in dictHashHdl or child.nodeName == '__setting':
                continue
            dictHashHdl[child.nodeName] = True
            str_result += (not_first and ("," + str_newline) or '')
            not_first = True
            dictChildSetting = None
            if (dictSetting is not None) and (child.nodeName in dictSetting):
                dictChildSetting = dictSetting[child.nodeName]
                if dictChildSetting is not None:
                    tp = dictChildSetting['_type']
                    if tp == 2:
                        str_result += parseXmlDict(dictChildSetting, parent, child.nodeName, idn + str_newidn)
                        continue
                    if tp == 3:
                        str_result += parseXmlArray(dictChildSetting, parent, child.nodeName, idn + str_newidn)
                        continue
            str_result += idn + str_newidn + str_dot + child.nodeName + str_dot + ':'
            str_result += parseXmlNode(dictChildSetting, child, idn + str_newidn)
            continue
        if child.nodeType == 3:
            # xml节点间字符串值
            if not not_first:
                value = child.nodeValue.strip(' ').strip('\n').strip('\r').strip('\t')
                if len(value) > 0:
                    if strIsNumber.match(value) is None:
                        value = '"' + value + '"'
                    return value
            continue
        if child.nodeType == 8:
            # xml注释信息，不进行处理
            # print child.nodeValue 
            continue
        print('error type: ', child.nodeType, ',  name: ', child.nodeName)
    str_result += (not_first and str_newline or '') + idn + '}'
    return str_result


def parseXmlList(out_write):
    out_write.write(out_pre + '{' + str_newline)
    not_first = False
    for root, dirs, files in os.walk(in_xmls): 
        for file in files:
            nameRe = xmlNameRe.match(file)
            if nameRe is not None:
                file = os.path.join(root, file)
                print('deal with: ', file)
                dom = xml.dom.minidom.parse(file)
                dictSetting = parseXmlSetting(dom.documentElement)
                out_write.write(not_first and ("," + str_newline) or '')
                out_write.write(str_newidn + str_dot + nameRe.group(1) + str_dot + ':')
                out_write.write(parseXmlNode(dictSetting, dom.documentElement, '' + str_newidn))
                not_first = True
        break
    jsonNameRe = re.compile('(.+)\.' + in_file_end + '$')
    for root, dirs, files in os.walk(in_files): 
        for file in files:
            nameRe = jsonNameRe.match(file)
            if nameRe is not None:
                print('add json with: ', file)
                out_write.write(not_first and ("," + str_newline) or '')
                out_write.write(str_newidn + str_dot + nameRe.group(1) + str_dot + ':')
                out_write.write(open(os.path.join(root, file)).read())
                not_first = True
        break
    out_write.write(str_newline + '}' + str_newline + out_end)

def write():
    with open(out_file, 'w') as file:
        parseXmlList(file)



