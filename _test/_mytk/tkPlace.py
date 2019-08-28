#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

# place: 
# - x	        指定组件的 X 坐标。x 为 0 代表位于最左边。
# - y	        指定组件的 Y 坐标。y 为 0 代表位于最右边。
# - relx	    指定组件的 X 坐标，以父容器总宽度为单位 1，该值应该在 0.0~1.0 之间，其中 0.0 代表位于窗口最左边，1.0 代表位于窗口最右边，0.5 代表位于窗口中间。
# - rely	    指定组件的 Y 坐标，以父容器总高度为单位 1，该值应该在 0.0~1.0  之间，其中 0.0 代表位于窗口最上边，1.0 代表位于窗口最下边，0.5 代表位于窗口中间。
# - width	    指定组件的宽度，以 pixel 为单位。
# - height	    指定组件的高度，以 pixel 为单位。
# - relwidth	指定组件的宽度，以父容器总宽度为单位 1，该值应该在 0.0~1.0 之间，其中 1.0 代表整个窗口宽度，0.5 代表窗口的一半宽度。
# - relheight	指定组件的高度，以父容器总高度为单位 1，该值应该在 0.0~1.0 之间，其中 1.0 代表整个窗口高度，0.5 代表窗口的一半高度。
# - bordermode  该属性支持“inside”或“outside” 属性值，用于指定当设置组件的宽度、高度时是否计算该组件的边框宽度。

#-----------------------------------------------------------

def help(self):
    help(tk.Label.place)

#-----------------------------------------------------------

def testPlace(parent):
    frame = tk.Frame(parent, width=100, height=100)
    frame.pack()
    tk.Label(frame, text='NW', font=('Arial', 20)).place(x=10, y=10, anchor=tk.NW)
    tk.Label(frame, text='SE', font=('Arial', 20)).place(x=90, y=90, anchor=tk.SE)


