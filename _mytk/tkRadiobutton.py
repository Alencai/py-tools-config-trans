#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

def testRadioBtn(parent):
    def radio_event():
        print("testRadioBtn")
    txtvar = tk.StringVar()
    radio1 = tk.Radiobutton(parent, text='Option A', variable=txtvar, value='A', command=radio_event)
    radio2 = tk.Radiobutton(parent, text='Option B', variable=txtvar, value='B', command=radio_event)
    radio1.pack()
    radio2.pack()

