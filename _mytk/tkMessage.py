#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

def testMessage(parent):
    def print_ret(func, msg):
        ret = func(msg)
        print('testMessage', type(ret), ret)
    tk.Button(parent, text="info", command=lambda:print_ret(showMsgInfo, 'info')).pack()
    tk.Button(parent, text="error", command=lambda:print_ret(showMsgError, 'error')).pack()
    tk.Button(parent, text="warning", command=lambda:print_ret(showMsgWarning, 'warning')).pack()
    tk.Button(parent, text="question", command=lambda:print_ret(showAskQues, 'question')).pack()
    tk.Button(parent, text="ask YesNo", command=lambda:print_ret(showAskYesNo, 'ask YesNo')).pack()
    tk.Button(parent, text="ask OkCancel", command=lambda:print_ret(showAskOkCancel, 'ask OkCancel')).pack()

#-----------------------------------------------------------

# return <str> 'ok'
def showMsgInfo(msg, title='info'):
    return tkMessageBox.showinfo(title=title, message=msg) # parent=window

# return <str> 'ok'
def showMsgError(msg, title='error'):
    return tkMessageBox.showerror(title=title, message=msg)

# return <str> 'ok'
def showMsgWarning(msg, title='warning'):
    return tkMessageBox.showwarning(title=title, message=msg)

# return <str> 'yes / 'no'
def showAskQues(msg, title='question'):
    return tkMessageBox.askquestion(title=title, message=msg)

# return <bool> True / False
def showAskYesNo(msg, title='ask'):
    return tkMessageBox.askyesno(title=title, message=msg)

# return <bool> True / False
def showAskOkCancel(msg, title='ask'):
    return tkMessageBox.askokcancel(title=title, message=msg)




