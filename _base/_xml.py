#!/usr/bin/python
# -*-coding:utf-8-*-

import json
import io
import xml.dom.minidom

# -------------------------------------------------

from _base._funcs import *
from _base._str import *
from _base._re import *
from _base._file import *
from _base._static import *

# -------------------------------------------------

KEY_PATH_IN = 'path_in'
KEY_PATH_OUT = 'path_out'
KEY_AUTONUMBER = 'autonumber'
KEY_ISDIR = 'isdir'
KEY_HASH_IGNORE = 'ignore'
KEY_HASH_NUMBER = 'number'
KEY_HASH_STRING = 'string'
KEY_HASH_ARRAY = 'array'
KEY_HASH_DICTS = 'dict'
KEY_HASH_TUPLE = 'tuple'

str_indent = '    '

# -------------------------------------------------

class MyParserXml:
    __settings = []
    
    # 转化属性类型
    def _transAttrValue(self, value, setting, full_name):
        to_number = (full_name in setting[KEY_HASH_NUMBER])
        to_string = (full_name in setting[KEY_HASH_STRING])
        if to_number or (setting[KEY_AUTONUMBER] and not to_string):
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

    # 获取配置tuple的json
    def _getJsonXmlTuple(self, node, setting, pre_name):
        ret_json = []
        for child_node in node.childNodes:
            if child_node.nodeType == 1:
                node_name = child_node.nodeName
                full_name = pre_name + '.' + node_name
                ret_json.append({
                    'name': node_name,
                    'data': self._getJsonXmlNode(child_node, setting, full_name),
                })
        return ret_json

    # 设置节点的json的标签值
    def _getJsonXmlChild(self, node, child_node, node_name, setting, pre_name):
        full_name = pre_name + '.' + node_name
        if full_name in setting[KEY_HASH_DICTS]:
            str_key = setting[KEY_HASH_DICTS][full_name]
            return self._getJsonXmlDict(node, node_name, str_key, setting, full_name)
        if full_name in setting[KEY_HASH_ARRAY]:
            return self._getJsonXmlArray(node, node_name, setting, full_name)
        return self._getJsonXmlNode(child_node, setting, full_name)
    
    # 设置节点的json的属性值
    def _setJsonXmlAttrs(self, node, setting, ret_json, pre_name):
        for key in node.attributes.keys():
            full_name = pre_name + '.' + key
            if full_name in setting[KEY_HASH_IGNORE]:
                continue
            value = node.getAttribute(key)
            ret_json[key] = self._transAttrValue(value, setting, full_name)
        pass
    
    # 获取节点的json
    def _getJsonXmlNode(self, node, setting, pre_name):
        ret_json = {}
        self._setJsonXmlAttrs(node, setting, ret_json, pre_name)
        if pre_name in setting[KEY_HASH_TUPLE]:
            str_name = setting[KEY_HASH_TUPLE][pre_name]
            if type(str_name) == str:
                ret_json[str_name] = self._getJsonXmlTuple(node, setting, pre_name)
            return ret_json
        hash_nodes = {}
        for child_node in node.childNodes:
            # # 正常节点信息（nodeType： 1节点标签内容、 3节点标签间首个text、 8注释内容）
            # print("xml node: type = %d, name = %s, value = %s" % (child_node.nodeType, child_node.nodeName, child_node.nodeValue))
            if child_node.nodeType == 3:
                if len(node.childNodes) == 1 and len(ret_json.keys()) == 0:
                    value = (child_node.nodeValue or "").strip(' \n\r\t\b')
                    return self._transAttrValue(value, setting, pre_name)
            if child_node.nodeType == 1:
                node_name = child_node.nodeName
                if node_name in hash_nodes:
                    continue
                hash_nodes[node_name] = True
                full_name = pre_name + '.' + node_name
                if full_name in setting[KEY_HASH_IGNORE]:
                    continue
                ret_json[node_name] = self._getJsonXmlChild(node, child_node, node_name, setting, pre_name)
        return ret_json
    
    #-----------------------------------------------------------------------------------
    
    # 返回json字符串
    def _exportJsonStr(self, ele_root, setting):
        ret_json = self._getJsonXmlNode(ele_root, setting, 'root')
        ret_str = json.dumps(ret_json, sort_keys = True, indent = 4) # encoding = 'utf-8'
        return deUnicode(ret_str)

    # 导出单个文件
    def _exportEachFile(self, setting, file_in, file_out, in_dir, out_dir, out_type):
        llog('________')
        llog('From file: %s' % file_in)
        try:
            xml_dom = xml.dom.minidom.parse(file_in)
            assert xml_dom, ('Error: can not find file: %s' % (file_in))
            ele_root = xml_dom.documentElement
            assert ele_root, ('Error: can not find root element')
            write_path, json_str = None, None
            if out_type == TYPE_JSON and file_out:
                write_path = os.path.join(out_dir, file_out + '.json')
                json_str = self._exportJsonStr(ele_root, setting)
            assert json_str, 'Error: Can not find json str'
            writeFile(json_str, write_path)
        except Exception as e:
            lerr(e)
        pass
    
    # 导出整个文件夹
    def _exportDirFile(self, setting, file_in, file_out, in_dir, out_dir, out_type):
        search_dir = os.path.abspath(os.path.join(in_dir, file_in))
        out_dir = os.path.abspath(os.path.join(out_dir, file_out))
        if os.path.isdir(search_dir):
            for root, dirs, files in os.walk(search_dir, topdown=True):
                for name in files:
                    file_in = os.path.join(root, name)
                    file_out = os.path.join(root.replace(search_dir, out_dir), removeSuffix(name))
                    self._exportEachFile(setting, file_in, file_out, in_dir, out_dir, out_type)
        pass

    #-----------------------------------------------------------------------------------
    
    # 读取xml字段配置表
    # <table path_in="dir_in" path_out="dir_out" autonumber="1" isdir="1">
    #     <number> person.man.id </number>
    #     <string> person.man.name </string>
    # </table>
    # <table path_in="xml1.xml" path_out="excel1" autonumber="1" isdir="1">
    #     <array> animal.pet </array>
    #     <dict key="id"> animal.pet.cat </dict>
    # </table>
    def parseSettingXml(self, file_name):
        self.__settings = []
        xml_dom = xml.dom.minidom.parse(file_name)
        assert xml_dom, ('error: can not find file: %s' % (file_name))
        ele_root = xml_dom.documentElement
        ele_sets = ele_root.getElementsByTagName('table')
        for setting in ele_sets:
            item = {}
            item[KEY_PATH_IN] = setting.getAttribute(KEY_PATH_IN)
            item[KEY_PATH_OUT] = setting.getAttribute(KEY_PATH_OUT)
            item[KEY_AUTONUMBER] = (setting.getAttribute(KEY_AUTONUMBER) == '1')
            item[KEY_ISDIR] = (setting.getAttribute(KEY_ISDIR) == '1')
            item[KEY_HASH_IGNORE] = self._getHashValues(setting, KEY_HASH_IGNORE)
            item[KEY_HASH_NUMBER] = self._getHashValues(setting, KEY_HASH_NUMBER)
            item[KEY_HASH_STRING] = self._getHashValues(setting, KEY_HASH_STRING)
            item[KEY_HASH_ARRAY] = self._getHashValues(setting, KEY_HASH_ARRAY)
            item[KEY_HASH_DICTS] = self._getHashValues(setting, KEY_HASH_DICTS, 'key')
            item[KEY_HASH_TUPLE] = self._getHashValues(setting, KEY_HASH_TUPLE, 'name')
            self.__settings.append(item)
        # print(self.__settings)
        pass

    # 导出配置到文件
    def exportFiles(self, in_dir, out_dir, out_type):
        llog('\n-------------------------------------------------------<<<<')
        llog('Begin Export Xml Files: ')
        reloadSys()
        createDir(out_dir)
        for setting in self.__settings:
            is_dir = setting[KEY_ISDIR]
            file_in = setting[KEY_PATH_IN]
            file_out = setting[KEY_PATH_OUT]
            if is_dir:
                self._exportDirFile(setting, file_in, file_out, in_dir, out_dir, out_type)
                continue
            file_in = os.path.abspath(os.path.join(in_dir, file_in))
            file_out = os.path.abspath(os.path.join(out_dir, file_out))
            self._exportEachFile(setting, file_in, file_out, in_dir, out_dir, out_type)
        llog('\nEnd Export.')
        pass



