#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

def testButton(parent):
    def btn_event():
        print("testButton")
    btn = tk.Button(parent, text="hit me", font=('Arial', 12), width=10, height=1)
    btn.configure(command=btn_event)
    btn.pack()

