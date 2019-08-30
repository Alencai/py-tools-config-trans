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

# https://docs.python.org/3/library/tkinter.html
# https://tkdocs.com/tutorial/index.html
# https://www.cnblogs.com/shwee/p/9427975.html
# http://c.biancheng.net/python/tkinter/


class MyTestUI(TkBase):
    _frame = None

    def __init__(self, *args, **kwargs):
        super(MyTestUI, self).__init__(*args, **kwargs)
        self._frame = tkScrollbar.getVScrollFrame(self._window)

    def renderTests(self):
        tests = [
            ['Label',      tkLabel.testLabel],
            ['Button',     tkButton.testButton],
            ['Entry',      tkEntry.testEntry],
            ['Text',       tkText.testText],
            ['Scrollbar',  tkScrollbar.testScrollbar],
            ['Radiobutton',tkRadiobutton.testRadioBtn],
            ['Checkbutton',tkCheckbutton.testCheckBtn],
            ['Scale',      tkScale.testScale],
            ['ListBox',    tkListbox.testListbox],
            ['Canvas',     tkCanvas.testCanvas],
            ['Frame',      tkFrame.testFrame],
            ['Combobox',   ttkCombobox.testCombobox],
            ['Pack',       tkPack.testPack],
            ['Place',      tkPlace.testPlace],
            ['Grid',       tkGrid.testGrid],
            ['Message',    tkMessage.testMessage],
        ]
        for menu in tests:
            menu[1](tkFrame.putFrameRowWithName(self._frame, menu[0], randomRGB()))
            menu[1] = lambda name=menu[0],func=menu[1]:func(tkWindow.newEmpty(self._window, name))
        tests.append(['Window', lambda:tkWindow.testWindow(self._window)])
        tkMenu.testMenuBar(self._window, tests)



