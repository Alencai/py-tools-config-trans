#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *
from _mytk.tkMessage import *

#-----------------------------------------------------------

__testCbVar = None # 必须存全局，否则会被释放，导致默认值显示为空
def testCombobox(parent):
    __testCbVar = tk.StringVar()
    cb = ttk.Combobox(parent, font=24, textvariable=__testCbVar)
    cb['values'] = ('Python', 'Swift', 'Kotlin')
    cb['state'] = 'readonly'
    # cb['postcommand'] = lambda: showMsgInfo(cb.get()) # 点击comb时触发
    cb.bind('<<ComboboxSelected>>', lambda evt:showMsgInfo(cb.get())) # 选择item后触发
    cb.pack(fill=tk.X, expand=tk.YES)
    cb.current(1)
    print('_testComboBox: %s, %s' % (cb.get(), __testCbVar.get()))
