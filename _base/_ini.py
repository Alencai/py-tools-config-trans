#! /usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json

# -------------------------------------------------

from _base._static import *
from _base._str import *

# -------------------------------------------------

if IS_PY2: 
    from ConfigParser import ConfigParser
else:
    from configparser import ConfigParser

#--------------------------------------------------------------------------
####### configparser #######
# 读取
# -read(filename)              直接读取文件内容
# -sections()                  得到所有的section，并以列表的形式返回
# -options(section)            得到该section的所有option
# -items(section)              得到该section的所有键值对
# -get(section,option)         得到section中option的值，返回为string类型
# -getint(section,option)      得到section中option的值，返回为int类型
# -getboolean(section,option)  得到section中option的值，返回为boolean类型
# -getfloat(section,option)    得到section中option的值，返回为float类型
# -has_section(section)        判断是否存在section
# -has_option(section,option)  判断是否存在option

# 写入
# -write(fp)                         将config对象写入至某个文件
# -add_section(section)              添加一个新的section
# -set(section, option, value)       对section中的option进行设置
# -remove_section(section)           删除某个 section
# -remove_option(section, option)    删除某个 section 下的 option
#--------------------------------------------------------------------------

class MyParserIni(ConfigParser):
    __filename = None

    #----------------------------------------
    
    def __checkFile(self, filename):
        if not os.path.exists(filename):
            open(filename, 'w')
        pass
    
    #----------------------------------------

    def read(self, filename):
        if filename:
            self.__checkFile(filename)
            if IS_PY2:
                import codecs
                file = codecs.open(filename, 'r', 'utf-8-sig')
                ConfigParser.readfp(self, file) 
            else:
                # super(MyParser, self).read(filename) 可指定为当前类的父类
                # super().read(filename) 
                ConfigParser.read(self, filename)
        self.__filename = filename
        pass
    
    def clear(self):
        for secname in self.sections():
            self.remove_section(secname)
        pass

    def reload(self):
        self.clear()
        self.read(self.__filename)
        pass
    
    def save(self, jsondata=None, savename=None):
        savename = savename or self.__filename
        str_ret = ''
        if jsondata:
            for secname in jsondata:
                item = jsondata[secname]
                str_ret += "[" + secname + "]\n"
                for optname in item:
                    str_ret += optname + "=" + item[optname] + "\n"
            # self.read_dict(jsondata) # py3有这个方法，可直接从dict读取ini内容
        with io.open(savename, mode='w', encoding='UTF-8') as file:
            file.write(str_ret)
        pass
    
    def toJson(self):
        rets = {}
        for secname in self.sections():
            item = {}
            for optname in self.options(secname):
                item[optname] = self.get(secname, optname)
            rets[secname] = item
        return rets
    
    def dumpIni(self):
        for secname in self.sections():
            print("[" + secname + "]")
            for option in self.options(secname):
                print("   " + option + " = " + self.get(secname, option))
            # for item in self.items(secname):
            #     print(item)
        pass
    
    def dumpJson(self):
        ret_json = self.toJson()
        ret_str = json.dumps(ret_json, sort_keys=False, indent=4)
        print(ret_str)
        pass



