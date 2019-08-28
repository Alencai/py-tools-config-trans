#!/usr/bin/python
# -*- coding: utf-8 -*-  
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

#-----------------------------------------------------------

import _mytk

ui = _mytk.MyTestUI()
ui.setTitle('tkinter测试')
ui.setSize(600, 600)
ui.renderTests()
ui.start()



