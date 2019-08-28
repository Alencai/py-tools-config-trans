#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

def testScale(parent):
    def print_scale(v):
        print("testScale", v)
    scale = tk.Scale(parent, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_scale)
    scale.pack()

