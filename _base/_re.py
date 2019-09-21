
import re

re_suffix_name = "^.+\.(.+)$"

# --------------------------------------------------------------------

def getDigit(txt):
    # return txt.isdigit() # txt需是utf8编码 
    ret = re.search('^(\d+)$', txt)
    return ret and ret.group(1) or None

def getInt(txt):
    ret = re.search('^(-?\d+)$', txt)
    return ret and ret.group(1) or None

def getDouble(txt):
    ret = re.search('^(-?\d*(?:\.\d+)?)$', txt)
    return ret and ret.group(1) or None

def getExcelInt(txt):
    if len(txt) == 0:
        return "0"
    ret = re.search('^(-?\d+)(?:\.0)?$', txt)
    return ret and ret.group(1) or None

def getExcelDouble(txt):
    if len(txt) == 0:
        return "0"
    return getDouble(txt)

# 获取文件名的后缀
def getSuffix(name):
    ret = re.search(re_suffix_name, name)
    return ret and ret.group(1) or None

# 判断文件名的后缀（如: json）
def checkSuffix(name, suffix):
    return getSuffix(name) == suffix



