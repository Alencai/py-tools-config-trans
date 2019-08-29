#!/usr/bin/python
# -*- coding: utf-8 -*-  
 
from _proj import *

if __name__ == "__main__":
    ui = MainUI()
    ui.parseIni('config.ini')
    ui.refreshList()
    ui.start()

