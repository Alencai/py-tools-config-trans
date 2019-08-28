#!/usr/bin/python
# -*- coding: utf-8 -*-  

import sys
import random

IS_PY2 = (sys.version_info[0] == 2)

if IS_PY2: 
    import Tkinter as tk
    import tkMessageBox
    import ttk
else:
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
    from tkinter import ttk


def randomColor():
    nums = '0123456789ABCDEF'
    color = '#'
    for i in range(6):
        color += nums[random.randint(0, 15)]
    return color

