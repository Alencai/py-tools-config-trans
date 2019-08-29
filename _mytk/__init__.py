#!/usr/bin/python
# -*- coding: utf-8 -*-  

import _mytk.tkPack as tkPack
import _mytk.tkGrid as tkGrid
import _mytk.tkPlace as tkPlace

import _mytk.tkMenu as tkMenu
import _mytk.tkScrollbar as tkScrollbar
import _mytk.tkLabel as tkLabel
import _mytk.tkButton as tkButton
import _mytk.tkEntry as tkEntry
import _mytk.tkText as tkText
import _mytk.tkRadiobutton as tkRadiobutton
import _mytk.tkCheckbutton as tkCheckbutton
import _mytk.tkScale as tkScale
import _mytk.tkListbox as tkListbox
import _mytk.tkCanvas as tkCanvas
import _mytk.tkFrame as tkFrame
import _mytk.ttkCombobox as ttkCombobox
import _mytk.tkWindow as tkWindow
import _mytk.tkMessage as tkMessage

from _mytk.tkHeaders import *
from _mytk.tkBase import *

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

# https://www.cnblogs.com/shwee/p/9427975.html
# http://c.biancheng.net/python/tkinter/

class MyTestUI(TkBase):
    _frame = None
    _listwins = []

    def __init__(self, *args, **kwargs):
        super(MyTestUI, self).__init__(*args, **kwargs)
        self._frame = tkScrollbar.getVScrollFrame(self._window)
    
    # -------------------------------------------------

    def addFrame(self, name, func1=None, func2=None):
        frame = tk.Frame(self._frame, bg=randomColor())
        frame.pack(fill=tk.X)
        label = tk.Label(frame, text=name)
        label.pack(side=tk.TOP, anchor=tk.NW)
        sub = tk.Frame(frame)
        sub.pack(fill=tk.X, padx=10, pady=10)
        func1 and func1(sub)
        func2 and self.addWindow(name, lambda:func2(tkWindow.newEmpty(self._window, name)))
    
    def addWindow(self, name, func):
        self._listwins.append([name, func])

    def renderTests(self):
        self.addWindow('Window', lambda:tkWindow.testWindow(self._window))
        self.addFrame('Label',      tkLabel.testLabel,         tkLabel.testLabel)
        self.addFrame('Button',     tkButton.testButton,       tkButton.testButton)
        self.addFrame('Entry',      tkEntry.testEntry,         tkEntry.testEntry)
        self.addFrame('Text',       tkText.testText,           tkText.testText)
        self.addFrame('Scrollbar',  tkScrollbar.testScrollbar, tkScrollbar.testScrollbar)
        self.addFrame('Radiobutton',tkRadiobutton.testRadioBtn,tkRadiobutton.testRadioBtn)
        self.addFrame('Checkbutton',tkCheckbutton.testCheckBtn,tkCheckbutton.testCheckBtn)
        self.addFrame('Scale',      tkScale.testScale,         tkScale.testScale)
        self.addFrame('ListBox',    tkListbox.testListbox,     tkListbox.testListbox)
        self.addFrame('Canvas',     tkCanvas.testCanvas,       tkCanvas.testCanvas)
        self.addFrame('Frame',      tkFrame.testFrame,         tkFrame.testFrame)
        self.addFrame('Combobox',   ttkCombobox.testCombobox,  ttkCombobox.testCombobox)
        self.addFrame('Pack',       tkPack.testPack,           tkPack.testPack)
        self.addFrame('Place',      tkPlace.testPlace,         tkPlace.testPlace)
        self.addFrame('Grid',       tkGrid.testGrid,           tkGrid.testGrid)
        self.addFrame('Message',    tkMessage.testMessage,     tkMessage.testMessage)
        tkMenu.testMenuBar(self._window, self._listwins)


