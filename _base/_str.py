#! /usr/bin/python
# -*- coding: UTF-8 -*-

import io
import random

from _base._static import IS_PY2, IS_PY3

# ---------------------------------------------------------------------
# 大小写转换

# print(str.upper())      # 把所有字符中的小写字母转换成大写字母
# print(str.lower())      # 把所有字符中的大写字母转换成小写字母
# print(str.capitalize()) # 把第一个字母转化为大写字母，其余小写
# print(str.title())      # 把每个单词的第一个字母转化为大写，其余小写 

# ---------------------------------------------------------------------

# 16进制字符
__HEX_CHARS = '0123456789ABCDEF'

# 获取16进制字符下标
def getHexCharIdx(char):
    return __HEX_CHARS.find(char.upper(), 0)

# 对16进制字符取反
def revertHexChar(char):
    idx = getHexCharIdx(char)
    return idx < 0 and char or __HEX_CHARS[15 - idx]
    
# 对16进制字符串取反
def reverseHexStr(txt):
    txt = ''.join([revertHexChar(char) for char in txt])
    return txt

# ---------------------------------------------------------------------

# 获取随机颜色
def randomRGB():
    color = '#' + ''.join([__HEX_CHARS[random.randint(0, 15)] for i in range(6)])
    return color

# 获取颜色取反
def reverseRGB(color):
    return reverseHexStr(color)

# 获取差距较大的颜色（用于文字反差背景）
def diverseRGB(color):
    rets = []
    for char in color:
        idx = getHexCharIdx(char)
        rets.append(idx < 0 and char or __HEX_CHARS[idx < 8 and 15 or 0])
    color = ''.join(rets)
    return color

# ---------------------------------------------------------------------
# 字符编码 （默认系统编码为utf8）

# - py2: [str -> unicode]
# - py3: [str -> str] # 不需要
def deUTF8(txt):
    if IS_PY2 and type(txt).__name__ == 'str' and hasattr(txt, 'decode'):
        txt = txt.decode("utf-8")
    return txt

# - py2: [unicode -> str] / [str -> str]
# - py3: [str -> str] # 不需要
def enUTF8(txt):
    if IS_PY2 and type(txt).__name__ == 'unicode' and hasattr(txt, 'encode'):
        txt = txt.encode("utf-8")
    return txt

# - py2: [str -> str]
# - py3: [bytes -> str] # 不需要
def deGBK(txt):
    if IS_PY2 and hasattr(txt, 'decode'):
        txt = txt.decode("GBK")
    return txt

# - py2: [str -> str]
# - py3: [str -> bytes] # 不需要
def enGBK(txt):
    if IS_PY2 and hasattr(txt, 'encode'):
        txt = txt.encode("GBK")
    return txt

# '\u7528\u6237' 转 '用户' （py2在终端显示有问题，写入文件时正确）  
# - py2: [str -> unicode -> str]
# - py3: [str -> bytes -> str]
def deUnicode(txt):
    if IS_PY3:
        if type(txt).__name__ == 'str' and hasattr(txt, 'encode'):
            txt = txt.encode("utf-8")
    if hasattr(txt, 'decode'):
        txt = txt.decode("unicode_escape")
    if IS_PY2:
        txt = txt.encode("utf-8")
    return txt

# '用户' 转 '\u7528\u6237' （py2在终端显示有问题，写入文件时正确）
# - py2: [unicode -> str] / [str -> unicode -> str]
# - py3: [str -> bytes -> str]
def enUnicode(txt): 
    if IS_PY2:
        if type(txt).__name__ == 'str' and hasattr(txt, 'decode'):
            txt = txt.decode("utf-8")
    if hasattr(txt, 'encode'):
        txt = txt.encode("unicode_escape")
    if IS_PY3:
        txt = txt.decode("utf-8")
    return txt

# 解码except报错信息 
def parseException(msg):
    tpn = type(msg).__name__
    if tpn == "str":
        return msg
    # if tpn == "AssertionError":
    if hasattr(msg, 'args') and len(msg.args) > 0:
        return msg.args[0]
    return 'unknow error'


# ---------------------------------------------------------------------

def fullStr(txt):
    return "\"" + txt + "\""

# ---------------------------------------------------------------------



