#! /usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

IS_PY2 = (sys.version_info[0] == 2)
IS_PY3 = (sys.version_info[0] == 3)
IS_WIN32 = (sys.platform == "win32")
IS_MAC = (sys.platform == "darwin")


BTN_FILE = 'file'
BTN_DIR  = 'dir'

TYPE_JSON = 'json'

