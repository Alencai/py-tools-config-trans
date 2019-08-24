
import re

# --------------------------------------------------------------------

def getDigit(str):
    # return str.isdigit() # str需是utf8编码 
    ret = re.search('^(\d+)$', str)
    return ret and ret.group(1) or None

def getInt(str):
    ret = re.search('^(-?\d+)$', str)
    return ret and ret.group(1) or None

def getDouble(str):
    ret = re.search('^(-?\d*(?:\.\d+)?)$', str)
    return ret and ret.group(1) or None

def getExcelInt(str):
    if len(str) == 0:
        return "0"
    ret = re.search('^(-?\d+)(?:\.0)?$', str)
    return ret and ret.group(1) or None

def getExcelDouble(str):
    if len(str) == 0:
        return "0"
    return getDouble(str)

# 获取后缀匹配字符串（比如*.json）
def getWithSuffix(name, suffix):
    ret = re.search('^(.*\.' + suffix + ')$', name)
    return ret and ret.group(1) or None



