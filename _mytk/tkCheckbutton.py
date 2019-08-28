#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

def testCheckBtn(parent):
    def check_event():
        print("testCheckBtn")
    intvar1 = tk.IntVar()
    intvar2 = tk.IntVar()
    check1 = tk.Checkbutton(parent, text='Option A', variable=intvar1, onvalue=1, offvalue=0, command=check_event)
    check2 = tk.Checkbutton(parent, text='Option B', variable=intvar2, onvalue=1, offvalue=0, command=check_event)
    check1.pack()
    check2.pack()


