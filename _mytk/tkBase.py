#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *
from traceback import format_exc
import _mytk.tkMessage as tkMessage
import _mytk.tkText as tkText

#-----------------------------------------------------------

class TkBase(object):
    _window = None      # 主窗口
    _tk_txt_log = None  # 日志类

    # -------------------------------------------------

    # def __new__(cls, *args, **kwargs):
    #     # return xxxxx

    def __init__(self, *args, **kwargs):
        # super传入的类，必须最终继承于object才有效
        super(TkBase, self).__init__()
        parent = self.__getArgParent(kwargs)
        if parent:
            self._window = tk.Toplevel(parent, *args, **kwargs)
        else:
            self._window = tk.Tk(*args, **kwargs)
        pass

    def __getArgParent(self, kwargs):
        if 'parent' in kwargs:
            parent = kwargs['parent']
            del kwargs['parent']
            return parent
        return None

    # -------------------------------------------------
    # checks

    def _checkStr(self, value):
        ret = False
        try:
            assert value and len(value.strip()) > 0, ('输入格式错误(%s)！' % (value or ''))
            ret = True
        except Exception as e:
            self.error(e)
        return ret

    def _checkFile(self, value):
        ret = False
        if self._checkStr(value):
            try:
                assert os.path.isfile(value), ('文件(%s)不存在！' % (value))
                ret = True
            except Exception as e:
                self.error(e)
        return ret

    def _checkDir(self, value):
        ret = False
        if self._checkStr(value):
            try:
                assert os.path.isdir(value), ('目录(%s)不存在！' % (value))
                ret = True
            except Exception as e:
                self.error(e)
        return ret
    
    # -------------------------------------------------
    # api:
    
    def setTitle(self, title):
        self._window.title(title)
        pass
    
    def setSize(self, width, height):
        self._window.geometry(str(width) + 'x' + str(height))
        pass

    # 设置不可调整尺寸：(0,0)
    def setResizable(self, width, height):
        self._window.resizable(width, height) 
        pass
    
    def start(self):
        self._window.mainloop()
        pass
    
    def exit(self):
        # self._window.quit()
        sys.exit()
        pass

    def log(self, msg):
        print(msg)
        if self._tk_txt_log:
            tkText.insertWithScrollText(self._tk_txt_log, msg + '\n')
        pass

    def error(self, msg):
        msg = parseException(msg)
        # format_stack() / print_stack() / print_exc() / print_exception() / format_exception()
        self.log('___________________________________')
        self.log(format_exc())
        self.log('[Error] ' + msg)
        self.log('---------------------------------<<')
        tkMessage.showMsgError(msg)
        pass

    def clearLog(self):
        tkText.clearWithScrollText(self._tk_txt_log)
        self.log('clear done!')
        pass



