#! /usr/bin/python
# -*- coding: UTF-8 -*-

import io, os, sys
import random

from _base._static import IS_WIN32, IS_PY2, IS_PY3
from _base._str import enGBK, deUTF8, fullStr

# ---------------------------------------------------------------------

def cmdStr(str):
    if IS_WIN32 and IS_PY2:
        return enGBK(deUTF8(fullStr(str)))
    return fullStr(str)

# 得到命令的返回值
def excSys(str):
    return os.system(cmdStr(str))

# 得到命令的输出
def excOpen(str):
    return os.popen(cmdStr(str))

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




