#! /usr/bin/python
# -*- coding: UTF-8 -*-

import random

from _base._static import *
from _base._str import *

# ---------------------------------------------------------------------

def cmdStr(str):
    if IS_WIN32:
        if IS_PY2:
            return enGBK(deUTF8(fullStr(str)))
    return fullStr(str)

# 命令返回值
def excSys(str):
    return os.system(cmdStr(str))

# 命令输出
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

# ---------------------------------------------------------------------

def randomColor():
    nums = '0123456789ABCDEF'
    color = '#'
    for i in range(6):
        color += nums[random.randint(0, 15)]
    return color


