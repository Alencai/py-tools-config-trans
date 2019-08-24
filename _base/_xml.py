#!/usr/bin/python
# -*-coding:utf-8-*-

import json
import io
import xml.dom.minidom

# -------------------------------------------------

from _base._str import *
from _base._re import *
from _base._file import *

# -------------------------------------------------

KEY_PATH = 'path'
KEY_JSONNAME = 'jsonname'
KEY_AUTONUMBER = 'autonumber'
KEY_HASH_NUMBER = 'hashNumber'
KEY_HASH_STRING = 'hashString'
KEY_HASH_ARRAY = 'hashArray'
KEY_HASH_DICTS = 'hashDicts'

str_indent = '    '

# -------------------------------------------------

class MyParserXml:
    __settings = []
    
    # 转化属性类型
    def _transAttrValue(self, value, setting, attr_name, pre_name):
        full_name = pre_name + (attr_name and ('.' + attr_name) or '')
        to_number = (full_name in setting[KEY_HASH_NUMBER])
        to_string = (full_name in setting[KEY_HASH_STRING])
        if to_number or (setting[KEY_AUTONUMBER] == '1' and not to_string):
            if getInt(value):
                value = int(value)
            elif getDouble(value):
                value = float(value)
        return value

    # 获取指定xml节点为键值对象
    def _getHashValues(self, setting, tag_name, attr_name = None):
        obj = {}
        values = setting.getElementsByTagName(tag_name)
        for value in values:
            key = 'root.' + value.childNodes[0].nodeValue.strip()
            obj[key] = attr_name and value.getAttribute(attr_name) or True
        return obj

    # 获取配置array的json
    def _getJsonXmlArray(self, node, node_name, setting, full_name):
        ret_json = []
        childs = node.getElementsByTagName(node_name)
        for child_node in childs:
            ret_json.append(self._getJsonXmlNode(child_node, setting, full_name))
        return ret_json

    # 获取配置dict的json
    def _getJsonXmlDict(self, node, node_name, str_key, setting, full_name):
        ret_json = {}
        childs = node.getElementsByTagName(node_name)
        for child_node in childs:
            key_value = child_node.getAttribute(str_key)
            if key_value:
                ret_json[key_value] = self._getJsonXmlNode(child_node, setting, full_name)
        return ret_json
    
    # 设置节点的json的属性值
    def _setJsonXmlAttrs(self, node, setting, ret_json, pre_name):
        for key in node.attributes.keys():
            value = node.getAttribute(key)
            ret_json[key] = self._transAttrValue(value, setting, key, pre_name)

    # 设置节点的json的标签值
    def _getJsonXmlChild(self, node, child_node, node_name, setting, pre_name):
        full_name = pre_name + '.' + node_name
        if full_name in setting[KEY_HASH_DICTS]:
            str_key = setting[KEY_HASH_DICTS][full_name]
            return self._getJsonXmlDict(node, node_name, str_key, setting, full_name)
        if full_name in setting[KEY_HASH_ARRAY]:
            return self._getJsonXmlArray(node, node_name, setting, full_name)
        return self._getJsonXmlNode(child_node, setting, full_name)
    
    # 获取节点的json
    def _getJsonXmlNode(self, node, setting, pre_name):
        ret_json = {}
        hash_nodes = {}
        self._setJsonXmlAttrs(node, setting, ret_json, pre_name)
        for child_node in node.childNodes:
            # # 正常节点信息（nodeType： 1节点标签内容、 3节点标签间首个text、 8注释内容）
            # print("xml node: type = %d, name = %s, value = %s" % (child_node.nodeType, child_node.nodeName, child_node.nodeValue))
            if child_node.nodeType == 3:
                if len(node.childNodes) == 1 and len(ret_json.keys()) == 0:
                    value = (child_node.nodeValue or "").strip(' \n\r\t\b')
                    return self._transAttrValue(value, setting, None, pre_name)
            if child_node.nodeType == 1:
                node_name = child_node.nodeName
                if node_name in hash_nodes:
                    continue
                hash_nodes[node_name] = True
                ret_json[node_name] = self._getJsonXmlChild(node, child_node, node_name, setting, pre_name)
        return ret_json
    
    #-----------------------------------------------------------------------------------
    
    # 返回json字符串
    def _exportJsonStr(self, ele_root, setting):
        ret_json = self._getJsonXmlNode(ele_root, setting, 'root')
        ret_str = json.dumps(ret_json, sort_keys = True, indent = 4) # encoding = 'utf-8'
        return deUnicode(ret_str)

    #-----------------------------------------------------------------------------------
    
    # 读取excel字段配置表
    # <table path="xml1.xml" sheetname="Sheet1" jsonname="excel1">
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
            item[KEY_JSONNAME] = setting.getAttribute('jsonname')
            item[KEY_AUTONUMBER] = setting.getAttribute('autonumber')
            item[KEY_HASH_NUMBER] = self._getHashValues(setting, 'number')
            item[KEY_HASH_STRING] = self._getHashValues(setting, 'string')
            item[KEY_HASH_ARRAY] = self._getHashValues(setting, 'array')
            item[KEY_HASH_DICTS] = self._getHashValues(setting, 'dict', 'key')
            self.__settings.append(item)
        # print(self.__settings)
    
    # 导出配置到文件
    def exportFiles(self, in_dir, out_dir):
        reloadSys()
        createDir(out_dir)
        for setting in self.__settings:
            file_name = os.path.join(in_dir, setting[KEY_PATH])
            json_file = setting[KEY_JSONNAME]
            xml_dom = xml.dom.minidom.parse(file_name)
            assert xml_dom, ('error: can not find file: %s' % (file_name))
            ele_root = xml_dom.documentElement
            if json_file:  # 导出json
                write_path = os.path.join(out_dir, json_file + '.json')
                json_str = self._exportJsonStr(ele_root, setting)
                writeFile(json_str, write_path)


