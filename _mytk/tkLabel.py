#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

def testLabel(parent):
    # tk.Label(parent, text='hello').pack()
    txtvar = tk.StringVar()
    txtvar.set('hello world')
    label = tk.Label(parent, textvariable=txtvar, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
    label.pack()

