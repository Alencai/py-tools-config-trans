#!/usr/bin/python
# -*- coding: utf-8 -*-  
 
from _base import *


# # 测试： range 、 enumerate 、 for 、 lambda
# li_data = range(2)
# # li_data = [0, 1]                           # 与上一样
# # li_data = [i for i in range(2)]            # 与上一样
# # li_data = [i for i in range(10) if i < 2]  # 与上一样
# en_data = enumerate(li_data)
# kv_data = {'a': 'apple', 'b': 'banana'}
# print(li_data)
# print(en_data)
# print(kv_data)
# for value in li_data:
#     print(value)
# for key, value in en_data:
#     print(key, value)
# for key in kv_data: 
#     print(key, kv_data.get(key)) 
# # for key, value in kv_data.items():     # 与上一样
# #     print(key, value)    
# # for key, value in dict.items(kv_data): # 与上一样
# #     print(key, value) 
# print('filter', filter(lambda x: x * x, range(5)))
# print('map', map(lambda x, y: (x or 1) * (y or 1), range(5), range(6)))
# print('reduce', reduce(lambda x, y: x + y, range(5)))  # 迭代，0+1+...+5
# fun1 = lambda:1
# fun2 = lambda x, y: x + y
# fun3 = lambda x, y: (x + y, x * y)
# fun4 = [(lambda x, y=i: x + y) for i in range(3)]
# print("--lambda 1. %d" % fun1())
# print("--lambda 2. %d" % fun2(1, 2))
# print("--lambda 3. %d %d" % fun3(2, 3))
# print("--lambda 4. %d" % fun4[1](4))


# # 示例： ini配置表
# parser = ini.MyParserIni()
# parser.read("config.ini")
# parser.dumpIni()
# parser.dumpJson()

# # 示例： xml配置表
# parser = xml.MyParserXml()
# parser.parseSettingXml("./example/xmls/setting.xml")
# parser.exportFiles('./example/xmls', ".out/xmls")

# # 示例： excel配置表
# parser = excel.MyParserExcel()
# parser.parseSettingXml("./example/excels/setting.xml")
# parser.exportFiles('./example/excels', ".out/excels")

# # 示例： 移除后缀文件
# removeWithSuffix(".out/excels", "json")

# # 示例： 字符串替换
# str_ret = replaceStr("abcdefg", "", "x", "[adf]")
# print(str_ret)

# # 示例： 测试UI
ui = myui.MyTestUI()
ui.setTitle('tkinter测试')
ui.setSize(600, 600)
ui.renderTests()
ui.start()


