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
# 字符编码

def deUTF8(txt):
    if IS_PY2:  # 相当于： '中文' 转 u'中文'  
        try:
            txt = txt.decode("utf-8")
        except:
            print('Error: deUTF8 %s', txt)
    return txt

def enUTF8(txt):
    if IS_PY2:
        try:
            txt = txt.encode("utf-8")
        except:
            print('Error: enUTF8 %s', txt)
    return txt

def deGBK(txt):
    if IS_PY2:
        try:
            txt = txt.decode('GBK')
        except:
            print('Error: deGBK %s', txt)
    return txt

def enGBK(txt):
    if IS_PY2:
        try:
            txt = txt.encode('GBK')
        except:
            print('Error: enGBK %s', txt)
    return txt

def deUnicode(txt):
    try:
        if IS_PY3:
            txt = txt.encode('utf-8')
        # 相当于： '\u7528\u6237' 转 '用户'  
        txt = txt.decode('unicode_escape')
    except:
        print('Error: deUnicode %s', txt)
    return txt

def enUnicode(txt):
    try:
        if IS_PY3:
            txt = txt.encode('utf-8')
        txt = txt.encode('unicode_escape')
    except:
        print('Error: enUnicode %s', txt)
    return txt

# ---------------------------------------------------------------------

def fullStr(txt):
    return "\"" + txt + "\""

# ---------------------------------------------------------------------



