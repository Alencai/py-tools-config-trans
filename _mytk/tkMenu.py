#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

def testPrint(*args):
    print('tkMenu', args)

# 测试一级菜单
def testMenuBar(parent, menudata):
    menu = tk.Menu(parent)
    menu.add_cascade(label='File', menu=testMenuSub2(menu))
    menu.add_cascade(label='Edit', menu=addMenus(parent, menu, menudata))
    parent.config(menu=menu)

# 测试二级菜单
def testMenuSub2(parent):
    menu = tk.Menu(parent, tearoff = 0)
    menu.add_command(label='Add', command=testPrint)
    menu.add_separator()
    menu.add_cascade(label='Sub', underline=0, menu=testMenuSub3(menu))
    menu.add_separator()  
    menu.add_command(label='Exit', command=lambda:sys.exit())
    return menu

# 测试三级菜单
def testMenuSub3(parent):
    menu = tk.Menu(parent)
    menu.add_command(label='Sub1', command=testPrint)
    menu.add_command(label='Sub2', command=testPrint)
    return menu

#-----------------------------------------------------------

# 添加菜单项
def addMenus(root, parent, menudata):
    menu = tk.Menu(parent, tearoff=0)
    for value in menudata:
        menu.add_command(label=value['name'], command=value['func'])
    return menu

