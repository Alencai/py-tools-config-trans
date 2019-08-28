#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

class TkBase(object):
    _window = None

    # -------------------------------------------------

    # def __new__(cls, *args, **kwargs):
    #     # return xxxxx

    def __init__(self, *args, **kwargs):
        # super传入的类，必须最终继承于object才有效
        super(TkBase, self).__init__(*args, **kwargs)
        parent = self.__getArgParent(**kwargs)
        if parent:
            self._window = tk.Toplevel(parent, *args, **kwargs)
        else:
            self._window = tk.Tk(*args, **kwargs)

    def __getArgParent(self, **kwargs):
        if 'parent' in kwargs:
            parent = kwargs['parent']
            del kwargs['parent']
            return parent
        return None

    # -------------------------------------------------
    # api:
    
    def setTitle(self, title):
        self._window.title(title)
    
    def setSize(self, width, height):
        # self._window.resizable(0, 0) # 设置不可调整尺寸
        self._window.geometry(str(width) + 'x' + str(height))
    
    def start(self):
        self._window.mainloop()
    
    def exit(self):
        # self._window.quit()
        sys.exit()



