#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

def testWindow(parent):
    ui = tk.Toplevel(parent)
    ui.title('tkinter弹窗')
    ui.geometry('200x200')
    tk.Button(ui, text="close", command=lambda:ui.destroy()).pack()


def newEmpty(parent, name, size='300x300'):
    ui = tk.Toplevel(parent)
    ui.title(name)
    ui.geometry(size)
    return ui


