#!/usr/bin/python
# -*- coding: utf-8 -*-  

from inspect import isfunction, ismethod
from _mytk.tkHeaders import *

#-----------------------------------------------------------

def _testPrint(*args):
    print('tkMenu._testPrint', args)

def testMenuBar(parent, cmds):
    menu = setMenuTopCmds(parent, [
        ['File', [  # 一级菜单 + 展开
            ['Add', _testPrint], # 二级菜单 + 事件
            [], # 分隔符
            ['Sub', [
                ['Sub1', _testPrint], # 三级菜单 + 事件
                ['Sub2', _testPrint],
            ]],
            ['Exit', lambda:sys.exit()],
        ]],
        ['Edit', cmds],
    ])
    menu.add_cascade(label='Help', underline=0, command=_testPrint) # 下划线

#-----------------------------------------------------------

# 添加菜单项
# cmds = [[label, command], [label, cmds], ...]
def setMenuCmds(parent, cmds):
    menu = tk.Menu(parent, tearoff=0)
    if len(cmds) == 2 and type(cmds[0]) == str: # 单个菜单，可直接传入
        cmds = [cmds] 
    for kv in cmds:
        if type(kv) == list and len(kv) == 2:
            # 下级菜单展开
            if type(kv[1]) == list:  
                menu.add_cascade(label=kv[0], menu=setMenuCmds(menu, kv[1]))
                continue
            # 绑定事件
            if isfunction(kv[1]) or ismethod(kv[1]): 
                menu.add_command(label=kv[0], command=kv[1])
                continue
        # 分隔符
        menu.add_separator() 
    return menu

def setMenuTopCmds(parent, cmds):
    menu = setMenuCmds(parent, cmds)
    parent.config(menu=menu)
    return menu


