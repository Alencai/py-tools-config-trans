#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _base._static import *

if IS_PY2: 
    import Tkinter as tk
    import tkMessageBox
    import ttk
else:
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
    from tkinter import ttk

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class TkBase(object):
    _window = None

    # -------------------------------------------------

    # def __new__(cls, *args, **kwargs):
    #     # return xxxxx
    
    def __init__(self, *args, **kwargs):
        # super传入的类，必须最终继承于object才有效
        super(TkBase, self).__init__()
        if 'parent' in kwargs:
            parent = kwargs['parent']
            del kwargs['parent']
            self._window = tk.Toplevel(parent, *args, **kwargs)
        else:
            self._window = tk.Tk(*args, **kwargs)

    # -------------------------------------------------
    # api:

    def setTitle(self, title):
        if self._window:
            self._window.title(title)
    
    def setSize(self, width, height):
        if self._window:
            # self._window.resizable(0, 0) # 设置不可调整尺寸
            self._window.geometry(str(width) + 'x' + str(height))

    def start(self):
        if self._window:
            self._window.mainloop()
    
    def exit(self):
        # if self._window:
        #     self._window.quit()
        sys.exit()


