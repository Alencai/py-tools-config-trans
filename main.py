#!/usr/bin/python
# -*- coding: utf-8 -*-  
 
from _base import *

if __name__ == "__main__":
    ui = myui.MyUI()
    ui.setTitle('配置表转化')
    ui.setSize(300, 400)
    ui.parseIni('config.ini')
    ui.start()

