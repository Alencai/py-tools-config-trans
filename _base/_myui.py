#!/usr/bin/python
# -*- coding: utf-8 -*-  
 
import os, sys

# -------------------------------------------------

from _base._static import *
from _base._str import *

import _base._ini as ini

# -------------------------------------------------

if IS_PY2: 
    import Tkinter
    import tkMessageBox
else:
    import tkinter as Tkinter
    import tkinter.messagebox as tkMessageBox

# -------------------------------------------------

# https://www.cnblogs.com/shwee/p/9427975.html

class MyUI:
    __ini_parser = None
    __root_window = None
    __top_scroll = None
    __top_list = None
    
    # -------------------------------------------------

    # def __new__(cls, *args, **kwargs):
    #     # return xxxxx
    
    def __init__(self, *args, **kwargs):
        self.__ini_parser = ini.MyParserIni()
        self.__root_window = Tkinter.Tk(**kwargs)
        self._renderMenuBar()
        self._renderScrollList()

    # -------------------------------------------------
    # render tests
    
    def _renderLabel(self):
        # label = Tkinter.Label(self.__root_window, text='hello')
        # label.pack()
        txtvar = Tkinter.StringVar()
        label = Tkinter.Label(self.__root_window, textvariable=txtvar, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
        label.pack()
        txtvar.set('hello world')
    
    def _renderBtn(self, parent):
        btn = Tkinter.Button(self.__root_window, text="hit me", font=('Arial', 12), width=10, height=1, command=self._onEvtEmptyJob)
        btn.pack()
    
    def _renderEntry(self):
        account = Tkinter.Entry(self.__root_window, show=None, font=('Arial', 14))
        password = Tkinter.Entry(self.__root_window, show='*', font=('Arial', 14)) 
        account.pack()
        password.pack()

    def _renderText(self):
        entry = Tkinter.Entry(self.__root_window, show = None)
        entry.pack()
        txtvar = entry.get()
        txt = Tkinter.Text(self.__root_window, height=3)
        txt.pack()
        txt.insert('insert', txtvar) # 在光标处插入
        txt.insert('end', txtvar)    # 在末位插入
    
    def _renderFrame(self):
        frame = Tkinter.Frame(self.__root_window)
        frame_l = Tkinter.Frame(frame)
        frame_r = Tkinter.Frame(frame)
        frame.pack()
        frame_l.pack(side='left')
        frame_r.pack(side='right')
        Tkinter.Label(frame, text='frame', bg='red', font=('Arial', 16)).pack()
        Tkinter.Label(frame_l, text='frame_l', bg='green').pack()
        Tkinter.Label(frame_r, text='frame_r', bg='yellow').pack()

    # -------------------------------------------------
    # render menu

    def _renderMenuBar(self):
        menu = Tkinter.Menu(self.__root_window)
        menu.add_cascade(labe='File', menu=self._renderMenuFile(menu))
        menu.add_cascade(labe='Edit', menu=self._renderMenuEdit(menu))
        self.__root_window.config(menu=menu)
    
    def _renderMenuFile(self, parent):
        menu = Tkinter.Menu(parent, tearoff = 0)
        menu.add_command(label='Add', command=self._onEvtEmptyJob)
        menu.add_separator()
        menu.add_cascade(label='Sub', underline=0, menu=self._renderMenuFileSub(menu))
        menu.add_separator()  
        menu.add_command(label='Exit', command=self.exit)
        return menu
    
    def _renderMenuFileSub(self, parent):
        menu = Tkinter.Menu(parent)
        menu.add_command(label='Sub1', command=self._onEvtEmptyJob)
        menu.add_command(label='Sub2', command=self._onEvtEmptyJob)
        return menu
    
    def _renderMenuEdit(self, parent):
        menu = Tkinter.Menu(parent, tearoff=0)
        menu.add_command(label='Edit', command=self._onEvtEmptyJob)
        return menu
    
    # -------------------------------------------------
    # render scroll listbox

    def _renderScrollList(self):
        self.__top_scroll = Tkinter.Scrollbar(self.__root_window) 
        self.__top_scroll.pack(side = Tkinter.RIGHT, fill = Tkinter.BOTH)
        self.__top_scroll.config(command=self._onEvtTopScrollYView)
        self.__top_list = Tkinter.Listbox(self.__root_window, width = 50, yscrollcommand = self._onEvtTopListYScroll)
        self.__top_list.bind('<ButtonRelease-1>', self._onEvtTopListSelect)
        self.__top_list.pack(side = Tkinter.LEFT, fill = Tkinter.BOTH)

    # -------------------------------------------------

    def _onEvtEmptyJob(self, *args):
        print("evt empty job!")
    
    def _onEvtTopScrollYView(self, *args):
        if self.__top_list:
            self.__top_list.yview(*args)

    def _onEvtTopListYScroll(self, *args):
        if self.__top_scroll:
            self.__top_scroll.set(*args)

    def _onEvtTopListSelect(self, evt):
        for itemIdx in self.__top_list.curselection():
            print(itemIdx)
        print(self, evt)

    # -------------------------------------------------

    def setTitle(self, title):
        if self.__root_window:
            self.__root_window.title(title)
    
    def setSize(self, width, height):
        if self.__root_window:
            self.__root_window.geometry(str(width) + 'x' + str(height))

    def start(self):
        if self.__root_window:
            self.__root_window.mainloop()
    
    def exit(self):
        # if self.__root_window:
        #     self.__root_window.quit()
        sys.exit()

    def parseIni(self, ini_path):
        self.__ini_parser.read("config.ini")
        self.updateTopList(self.__ini_parser.toJson())
    
    def showMsg(self, txt, title = 'msg'):
        tkMessageBox.showinfo(title, txt, parent = self.__root_window)
        
    def addTopListItem(self, name, data):
        if self.__top_list:
            self.__top_list.insert(Tkinter.END, name)

    def clearTopList(self):
        if self.__top_list:
            self.__top_list.delete(0, self.__top_list.size())

    def updateTopList(self, datas):
        self.clearTopList()
        for key in datas.keys():
            self.addTopListItem(key, datas[key])
    

