#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _base import *

if IS_PY2: 
    import Tkinter as tk
    import tkMessageBox
    import ttk
    import tkFileDialog as tkdlg
else:
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
    from tkinter import ttk
    from tkinter import filedialog as tkdlg





