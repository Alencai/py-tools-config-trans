#!/usr/bin/python
# -*- coding: utf-8 -*-  

import os

_ini_default = 'config.ini'
_ini_cfg_trans = 'example/cfg_trans/config.ini'

def check_ini_path(other_default):
    if os.path.exists(_ini_default):
        return _ini_default
    if os.path.exists(other_default):
        return other_default
    return _ini_default

def create_cfg_trans():
    from _projs.cfg_trans import MainUI
    ui = MainUI()
    ui.parseIni(check_ini_path(_ini_cfg_trans))
    ui.refreshList()
    ui.start()
    pass

if __name__ == "__main__":
    create_cfg_trans() # 配置表转化




