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



