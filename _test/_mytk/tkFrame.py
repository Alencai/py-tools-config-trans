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



