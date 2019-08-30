#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

import random

#-----------------------------------------------------------

def testText(parent):
    txt = tk.Text(parent, height=3) # 这里hight是行数
    txt.pack()
    frame = tk.Frame(parent)
    frame.pack()
    def mark_move():
        txt.focus_set()
        cur = txt.get('1.0', tk.END) # "1.0" 代表行列，行从1开始
        idx = random.randint(0, len(cur))
        txt.mark_set("insert", "1.%d" % idx)
    bt1 = tk.Button(frame, text="insert")
    bt2 = tk.Button(frame, text="end")
    bt3 = tk.Button(frame, text="move")
    bt1.configure(command=lambda:(txt.focus_set(),txt.insert(tk.INSERT, '-insert-'))) # 在光标处插入
    bt2.configure(command=lambda:(txt.focus_set(),txt.insert(tk.END, '-end-')))       # 在末位插入
    bt3.configure(command=mark_move)    # 随机设置光标位置
    bt1.grid(row=1, column=1)
    bt2.grid(row=1, column=2)
    bt3.grid(row=1, column=3)

#-----------------------------------------------------------

# 1. 获取一个滚动的，不可编辑的文本框
def putScrollTextView(parent, width):
    text = tk.Text(parent, height=8, state=tk.DISABLED)
    scroll = tk.Scrollbar(parent, orient=tk.VERTICAL, command=text.yview)
    scroll.place(relx=1, rely=0.5, relheight=1, anchor=tk.E)
    text.place(relx=0, rely=0.5, width=width-int(scroll['width']), relheight=1, anchor=tk.W)
    text.config(yscrollcommand=scroll.set)
    return text

# 1.1 对不可编辑的文本框插入数据
def insertWithScrollText(text, data):
    text.config(state=tk.NORMAL)
    text.insert(tk.END, data)
    text.config(state=tk.DISABLED)
    text.yview_moveto(1)




