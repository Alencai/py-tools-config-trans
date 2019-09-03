#! /usr/bin/python
# -*- coding: UTF-8 -*-

import os
import io
import sys
import shutil
import re
import zipfile
import hashlib

# -------------------------------------------------

from _base._str import *
from _base._re import *
from _base._log import *

#-----------------------------------------------------------------

# 创建[文件夹]
def createDir(dir):
    if os.path.exists(dir):
        return
    # os.mkdir(dir)  # 创建单个文件夹
    os.makedirs(dir) # 创建多级文件夹

# 移除[文件夹]
def removeDir(dir):
    # for root, dirs, files in os.walk(dir, topdown=False):
    #     for name in files:
    #         os.remove(os.path.join(root, name))
    #     for name in dirs:
    #         os.rmdir(os.path.join(root, name))
    shutil.rmtree(dir) # 可直接用这一句  

# 移除[文件/文件夹]
def removeFile(name):
    if os.path.exists(name):
        if os.path.isdir(name):
            removeDir(name)
        else:
            os.remove(name)

# 校验[上级目录]
def checkPreDir(dir):
    # name = os.path.basename(dir)
    dir = os.path.dirname(os.path.abspath(dir))
    createDir(dir)

# 浅复制[文件/文件夹]
def copyTo(origin, target):
    checkPreDir(target)
    if os.path.exists(origin):
        if os.path.isdir(origin):
            origin = os.path.abspath(origin)
            for root, dirnames, filenames in os.walk(origin):
                to_root = os.path.join(target, root[1 + len(origin):])
                for dir_name in dirnames:
                    createDir(os.path.join(to_root, dir_name))
                for file_name in filenames:
                    from_name = os.path.join(root, file_name)
                    to_name = os.path.join(to_root, file_name)
                    removeFile(to_name)
                    shutil.copyfile(from_name, to_name)
        else:
            removeFile(target)
            shutil.copyfile(origin, target)

# 强复制[文件/文件夹]（目标文件夹将被清空）
def copyReplace(origin, target):
    if os.path.exists(target):
        removeFile(target)
    checkPreDir(target)
    if os.path.exists(origin):
        if os.path.isdir(origin):
            shutil.copytree(origin, target)
        else:
            shutil.copyfile(origin, target)

#-----------------------------------------------------------------

# 获取[目录内]符合名字的文件
# 只遍历根目录
def getMatchName(target_dir, re_str):
    list = []
    re_match = re.compile(re_str)
    for root, dirnames, filenames in os.walk(target_dir):
        for file_name in filenames: 
            if re_match.match(file_name):
                return list.append(target_dir + file_name)
        break 
    return list

#-----------------------------------------------------------------

# 写文件
def writeFile(str_data, file_name):
    llog('write file: %s' % file_name)
    with io.open(file_name, mode='w+', encoding='UTF-8') as file:
        file.write(deUTF8(str_data))

# 写文件
def appendFile(str_data, file_name):
    llog('write file: %s' % file_name)
    with io.open(file_name, mode='a+', encoding='UTF-8') as file:
        file.write(deUTF8(str_data))

# 替换[字符串]
def replaceStr(str_data, str_old, str_new, re_str = None):
    if re_str:
        # rets = re.findall(re_str, str_data)
        # for rtuple in rets:
        #     str_old = rtuple[0]
        re_match = re.compile(re_str)
        str_data = re_match.sub(str_new, str_data)
    else:
        str_data = str_data.replace(str_old, str_new)
    return str_data

# 替换[文件文本]的[字符串]
def replaceFileStr(file_name, str_old, str_new, re_str = None):
    if not os.path.exists(file_name):
        return
    temp_file_name = file_name + '.rp.bak'
    with io.open(file_name, mode='r', encoding='UTF-8') as file_in:
        text = replaceStr(file_in.read(), str_old, str_new, re_str)
        with io.open(temp_file_name, mode='w', encoding='UTF-8') as file_out:
            file_out.write(text)
    os.remove(file_name)
    os.rename(temp_file_name, file_name)

#-----------------------------------------------------------------

# 压缩[文件/文件夹]
def zipFileTo(fileName, zipName):
    removeFile(zipName)
    fileName = os.path.abspath(fileName)
    filelist = []
    if os.path.isdir(fileName):
        for root, dirs, files in os.walk(fileName, topdown=True):
            for dir in dirs:
                filelist.append([root, dir])
            for name in files:
                name = os.path.join(root, name)
                filelist.append([fileName, name[1 + len(fileName):]])
    else:
        filelist.append([os.path.dirname(fileName), os.path.basename(fileName)])
    llog("create: %s" % zipName)
    zf = zipfile.ZipFile(zipName, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        llog(" - zip file: %s; %s" % (tar[0], tar[1]))
        zf.write(os.path.join(tar[0], tar[1]), tar[1])
    zf.close()

#-----------------------------------------------------------------

# 得到文件md5
def getFileMD5(fileName, isLog = True, block_size = 64*1024):
    str_md5 = "none"
    with open(fileName, 'rb') as f:
        md5 = hashlib.md5()
        while True:
            data = f.read(block_size)
            if data:
                md5.update(data)
            else:
                break
        str_md5 = md5.hexdigest()
    if isLog:
        llog("file = %s" % fileName)
        llog("md5 = %s, size = %d" % (str_md5, os.path.getsize(fileName)))
    return str_md5

# 得到目录内所有md5
def getDirMd5(dir):
    rets = []
    dir = os.path.abspath(dir)
    for rootdir, subdirs, names in os.walk(dir):
        for name in names: 
            if name[0] == '.':
                continue
            path = os.path.join(rootdir, name)
            rets.append({
                "name": path.replace(dir, "").replace("\\", "/")[1:],
                "md5": getFileMD5(path, False),
                "size": os.path.getsize(path),
            })
    return rets

# ---------------------------------------------------------------------

# 移除目录内所有后缀文件（比如*.json）
def removeWithSuffix(dir, suffix):
    for root, dirs, files in os.walk(dir): 
        for file in files:
            if getWithSuffix(file, suffix):
                os.remove(os.path.join(root, file))








