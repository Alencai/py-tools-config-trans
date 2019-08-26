#!/usr/bin/python
# -*- coding: utf-8 -*-  
 
import os, sys

# -------------------------------------------------

from _base._mytestui import *

import _base._ini as ini

# -------------------------------------------------

class MyUI(MyBaseUI):
    _iniParser = None
    _scroll = None
    _list = None
    
    # -------------------------------------------------

    def __init__(self, *args, **kwargs):
        super(MyUI, self).__init__(*args, **kwargs)
        self._iniParser = ini.MyParserIni()
    
    # -------------------------------------------------
    # render scroll listbox

    def _renderScrollList(self):
        self._scroll = tk.Scrollbar(self._window) 
        self._scroll.config(command=self._onEvtTopScrollYView)
        self._scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self._list = tk.Listbox(self._window, yscrollcommand=self._scroll.set)
        self._list.bind('<ButtonRelease-1>', self._onEvtTopListSelect)
        self._list.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

    # -------------------------------------------------
    # events

    def _onEvtTopScrollYView(self, *args):
        self._list and self._list.yview(*args)

    def _onEvtTopListSelect(self, evt):
        for itemIdx in self._list.curselection():
            print(itemIdx)
        print(self, evt)

    # -------------------------------------------------

    def addTopListItem(self, name, data):
        if self._list:
            self._list.insert(tk.END, name)

    def clearTopList(self):
        if self._list:
            self._list.delete(0, self._list.size())

    def updateScrollList(self, datas):
        self.clearTopList()
        for key in datas.keys():
            self.addTopListItem(key, datas[key])
    
    # -------------------------------------------------

    def parseIni(self, ini_path):
        self._iniParser.read(ini_path)

    def renderUI(self):
        self._renderScrollList()
        self.updateScrollList(self._iniParser.toJson())
        
    

