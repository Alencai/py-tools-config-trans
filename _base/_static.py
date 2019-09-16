#! /usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

IS_PY2 = (sys.version_info < (3, 0))
IS_PY3 = (sys.version_info >= (3, 0))
IS_WIN32 = (sys.platform == "win32")
IS_MAC = (sys.platform == "darwin")


BTN_FILE = 'file'
BTN_DIR  = 'dir'

TYPE_XML = 'xml'
TYPE_EXCEL = 'excel'
TYPE_JSON = 'json'

