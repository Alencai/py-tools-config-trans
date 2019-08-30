#!/usr/bin/python
# -*- coding: utf-8 -*-  
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

#-----------------------------------------------------------

from _base import *

#-----------------------------------------------------------

# # 示例： ini配置表
# parser = ini.MyParserIni()
# parser.read("../config.ini")
# parser.dumpIni()
# parser.dumpJson()

# # 示例： xml配置表
# parser = xml.MyParserXml()
# parser.parseSettingXml("./../example/xmls/setting.xml")
# parser.exportFiles('./../example/xmls', "./../.out/xmls")

# # 示例： excel配置表
# parser = excel.MyParserExcel()
# parser.parseSettingXml("./../example/excels/setting.xml")
# parser.exportFiles('./../example/excels', "./../.out/excels")

# # 示例： 移除后缀文件
# removeWithSuffix("./../.out/excels", "json")

# # 示例： 字符串替换
# str_ret = replaceStr("abcdefg", "", "x", "[adf]")
# print(str_ret)

# 示例： 颜色
color = randomRGB()
print(color, reverseRGB(color))





