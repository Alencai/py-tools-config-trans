#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

def testLabel(parent):
    # tk.Label(parent, text='hello').pack()
    txtvar = tk.StringVar()
    txtvar.set('hello world')
    tk.Label(parent, textvariable=txtvar, bg='green', fg='white', justify=tk.RIGHT).pack(side=tk.TOP)
    tk.Label(parent, text='hello', font=('Arial', 12), width=30, height=2).pack(side=tk.TOP)

