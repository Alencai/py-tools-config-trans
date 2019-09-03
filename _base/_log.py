#! /usr/bin/python
# -*- coding: UTF-8 -*-

import io
from _base._str import deUTF8

def lprint(msg):
    print(msg)

__llog = lambda msg: lprint(msg)
__lerr = lambda msg: lprint(msg)

def setllog(func):
    global __llog
    __llog = func

def setlerr(func):
    global __lerr
    __lerr = func

def llog(msg):
    __llog(msg)

def lerr(msg):
    __lerr(msg)

def wlog(msg, **kvargs):
    name = ('name' in kvargs) and kvargs['name'] or 'write.log'
    mode = ('mode' in kvargs) and kvargs['mode'] or 'w+'
    encoding = ('encoding' in kvargs) and kvargs['encoding'] or 'UTF-8'
    with io.open(name, mode=mode, encoding=encoding) as file:
        file.write(deUTF8(msg))
        file.write(deUTF8('\n'))
    pass



