#! /usr/bin/python
# -*- coding: UTF-8 -*-

import io

from _base._static import *

# ---------------------------------------------------------------------

def deUTF8(txt):
    if IS_PY2:
        return txt.decode("utf-8")
    return txt

def enUTF8(txt):
    if IS_PY2:
        return txt.encode("utf-8")
    return txt

def deGBK(txt):
    if IS_PY2:
        return txt.decode('GBK')
    return txt

def enGBK(txt):
    if IS_PY2:
        return txt.encode('GBK')
    return txt

def deUnicode(txt):  
    if IS_PY2: # '\u7528\u6237' 转 '用户'
        return txt.decode('unicode_escape')
    return txt.encode('utf-8').decode('unicode_escape')

def enUnicode(txt):
    if IS_PY2:
        return txt.encode('unicode_escape')
    return txt.encode('utf-8').encode('unicode_escape')

def fullStr(txt):
    return "\"" + txt + "\""

# ---------------------------------------------------------------------

def inputStr(txt):
    # py2的input输入整数时，类型是整数而非字符串
    if IS_PY2:
        return raw_input(txt) 
    return input(txt)

def reloadSys():
    if IS_PY2:
        reload(sys)
        sys.setdefaultencoding("utf-8")
    else:
        import importlib 
        importlib.reload(sys)



