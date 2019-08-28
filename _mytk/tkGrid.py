#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

# grid: 
# - column	    指定将组件放入哪列，第一列的索引为 0。
# - columnspan	指定组件横跨多少列。
# - row	        指定组件放入哪行，第一行的索引为 0。
# - rowspan 	指定组件横跨多少行。
# - sticky	    类似 pack() 方法的 anchor 选项，同样支持 N（北，代表上）、E（东，代表右）、S（南，代表下）、W（西，代表左）、NW（西北，代表左上）、NE（东北，代表右上）、SW（西南，代表左下）、SE（东南，代表右下）、CENTER（中，默认值）这些值。

#-----------------------------------------------------------

def help(self):
    help(tk.Label.grid)

#-----------------------------------------------------------

def testGrid(parent):
    entry = tk.Entry(parent, relief=tk.SUNKEN, font=('Courier New', 24), width=18)
    entry.pack(side=tk.TOP, pady=10)
    names = "0123456789+-*/.="
    frame = tk.Frame(parent) # grid不能与pack、place放到一起，否则会崩溃
    frame.pack(side=tk.TOP)
    for i in range(len(names)):
        btn = tk.Button(frame, text=names[i], font=('Verdana', 20), width=4)
        btn.configure(command=lambda chr=names[i]:entry.insert(tk.END, chr))
        btn.grid(row=i//4, column=i%4)




