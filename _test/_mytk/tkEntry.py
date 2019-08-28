#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

def testEntry(parent):
    account = tk.Entry(parent, text="123", show=None, font=('Arial', 14))
    password = tk.Entry(parent, text="456", show='*', font=('Arial', 14)) 
    # text = account.get()
    account.pack()
    password.pack()

