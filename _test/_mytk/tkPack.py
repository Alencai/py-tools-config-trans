#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

# pack: 
# - anchor	当可用空间大于组件所需求的大小时，该选项决定组件被放置在容器的何处。该选项支持 N（北，代表上）、E（东，代表右）、S（南，代表下）、W（西，代表左）、NW（西北，代表左上）、NE（东北，代表右上）、SW（西南，代表左下）、SE（东南，代表右下）、CENTER（中，默认值）这些值。
# - expand	该 bool 值指定当父容器增大时才是否拉伸组件。
# - fill	设置组件是否沿水平或垂直方向填充。该选项支持 NONE、X、Y、BOTH 四个值，其中 NONE 表示不填充，BOTH 表示沿着两个方向填充。
# - ipadx	指定组件在 x 方向（水平）上的内部留白（padding），默认为0。
# - ipady	指定组件在 y 方向（水平）上的内部留白（padding），默认为0。
# - padx	指定组件在 x 方向（水平）上与其他组件的间距，默认为0。
# - pady	指定组件在 y 方向（水平）上与其他组件的间距，默认为0。
# - side	设置组件的添加位置，可以设置为 TOP、BOTTOM、LEFT 或 RIGHT 这四个值的其中之一。

#-----------------------------------------------------------

def help(self):
    help(tk.Label.pack)

#-----------------------------------------------------------

def testPack(parent):
    tk.Label(parent, text='P', fg='red').pack(side=tk.TOP)    
    tk.Label(parent, text='P', fg='red').pack(side=tk.BOTTOM) 
    tk.Label(parent, text='P', fg='red').pack(side=tk.LEFT)   
    tk.Label(parent, text='P', fg='red').pack(side=tk.RIGHT)  


