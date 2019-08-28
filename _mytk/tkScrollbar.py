#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

def testScrollbar(parent):
    text = tk.Text(parent, height=5, width=10)
    text.insert(tk.INSERT, "1\n2\n3\n4\n5\n6\n7\n8\n9\n")
    text.pack(side=tk.LEFT)
    scroll = tk.Scrollbar(parent, orient=tk.VERTICAL, command=text.yview)
    scroll.pack(side=tk.LEFT, fill=tk.Y)
    text.config(yscrollcommand=scroll.set)
    
#-----------------------------------------------------------

# 获取竖直带滚动的frame
def getVScrollFrame(parent):
    canvas = tk.Canvas(parent)
    frame = tk.Frame(canvas)
    scroll = tk.Scrollbar(parent, orient=tk.VERTICAL)
    scroll.configure(command=canvas.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=scroll.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
    def resize_canvas(e):
        print("getVScrollFrame.resize_canvas: width=%d, height=%d" % (e.width, e.height))
        canvas.create_window(0, 0, anchor=tk.NW, window=frame, width=e.width)
        canvas.unbind("<Configure>")
    canvas.bind("<Configure>", resize_canvas)
    def resize_frame(e):
        print("getVScrollFrame.resize_frame: width=%d, height=%d" % (e.width, e.height))
        canvas.configure(scrollregion=(0, 0, 0, e.height))
        frame.unbind("<Configure>")
    frame.bind("<Configure>", resize_frame)
    return frame

#-----------------------------------------------------------


