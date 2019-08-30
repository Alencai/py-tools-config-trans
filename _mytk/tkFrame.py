#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

def testFrame(parent):
    frame1 = tk.Frame(parent)
    frame2 = tk.Frame(frame1)
    frame3 = tk.Frame(frame1)
    frame1.pack()
    frame2.pack(side='left')
    frame3.pack(side='right')
    tk.Label(frame1, text='frame', bg='red', font=('Arial', 16)).pack()
    tk.Label(frame2, text='frame_l', bg='green').pack()
    tk.Label(frame3, text='frame_r', bg='yellow').pack()

#-----------------------------------------------------------

def getFrameLeft(parent, width):
    frame = tk.Frame(parent, width=width)
    # frame.pack(side=tk.LEFT, fill=tk.Y)
    frame.place(relx=0, rely=0.5, width=width, relheight=1, anchor=tk.W)
    return frame

def getFrameRight(parent, width):
    frame = tk.Frame(parent, width=width)
    # frame.pack(side=tk.RIGHT, fill=tk.Y)
    frame.place(relx=1, rely=0.5, width=width, relheight=1, anchor=tk.E)
    return frame

def getFrameTop(parent, height):
    frame = tk.Frame(parent, height=height)
    # frame.pack(side=tk.TOP, fill=tk.X)
    frame.place(relx=0.5, rely=0, relwidth=1, height=height, anchor=tk.N)
    return frame

def getFrameBottom(parent, height):
    frame = tk.Frame(parent, height=height)
    # frame.pack(side=tk.BOTTOM, fill=tk.X)
    frame.place(relx=0.5, rely=1, relwidth=1, height=height, anchor=tk.S)
    return frame


#-----------------------------------------------------------

# 设置一个 label + entry + button 组合的 frame
# 1. label 最多7个中文字符  (80px)
# 2. button 最多4个中文字符 (60px)
def putFrameRowInput(parent, width, label_name, txtvar, btn_name=None, btn_cmd=None, btn_ext=None):
    frame = tk.Frame(parent, width=width, height=25)
    tk.Label(frame, text=label_name, justify=tk.LEFT).place(x=80, y=5, anchor=tk.NE)
    tk.Entry(frame, textvariable=txtvar).place(x=85, y=5, width=width-150, anchor=tk.NW)
    if btn_name and btn_cmd:
        btn = tk.Button(frame, text=btn_name, command=lambda:btn_cmd(txtvar.get(), btn_ext))
        btn.place(x=width, y=0, width=60, anchor=tk.NE)
    frame.pack(side=tk.TOP, ipady=5)
    return frame

# 设置一个 listbox
def putFrameRowCombobox(parent, width, label_name, txtvar, values):
    frame = tk.Frame(parent, width=width, height=25)
    tk.Label(frame, text=label_name, justify=tk.LEFT).place(x=80, y=5, anchor=tk.NE)
    cb = ttk.Combobox(frame, width=width - 150, values=values, textvariable=txtvar, state='readonly')
    cb.place(x=85, y=5, width=width-150, anchor=tk.NW)
    cb.current(1)
    frame.pack(side=tk.TOP, ipady=5)
    return frame

# 设置一条线
def putFrameRowLine(parent, width):
    frame = tk.Frame(parent)
    canvas = tk.Canvas(frame, width=width, height=8)
    canvas.create_line(10, 7, width - 10, 7)
    canvas.pack()
    frame.pack(side=tk.TOP, ipady=5)
    return frame

# 设置一堆按钮
def putFrameRowBtns(parent, *args):
    frame = tk.Frame(parent)
    for data in args:
        tk.Button(frame, width=12, text=data[0], command=data[1]).pack(side=tk.LEFT, padx=10)
    frame.pack(side=tk.TOP, ipady=5)
    return frame

# 获取一个带名字的Frame
def putFrameRowWithName(parent, name, bg='#ffffff'):
    frame = tk.Frame(parent, bg=bg)
    label = tk.Label(frame, text=name, fg=diverseRGB(bg), bg=bg)
    subfr = tk.Frame(frame)
    frame.pack(fill=tk.X)
    label.pack(side=tk.TOP, anchor=tk.NW)
    subfr.pack(fill=tk.X, padx=10, pady=10)
    return subfr
