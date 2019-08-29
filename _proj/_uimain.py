#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk import *
from _base import *

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class MainParsor(TkBase):
    _ini_parser = None  # ini - 解析类
    _ini_json = None    # ini - json数据
    # -------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(MainParsor, self).__init__(*args, **kwargs)
        self._ini_parser = ini.MyParserIni()
        self._ini_json = {}
        pass
    # --------------------------------------------
    def _writeIniParser(self):
        self._ini_parser.save(self._ini_json)
        pass
    def _getExportParser(self, proj_type):
        if proj_type == 'excel':
            return excel.MyParserExcel()
        if proj_type == 'xml':
            return xml.MyParserXml()
        return None
    # --------------------------------------------
    def parseIni(self, ini_path):
        self._ini_parser.read(ini_path)
        self._ini_json = self._ini_parser.toJson()
        pass

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class MainInputVar(MainParsor):
    _txtvar_key = None     # 项目键值
    _txtvar_name = None    # 项目名
    _txtvar_type = None    # 项目配置类型
    _txtvar_setting = None # 项目配置文件
    _txtvar_pathin = None  # 输入目录
    _txtvar_pathout = None # 输出目录
    # -------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(MainInputVar, self).__init__(*args, **kwargs)
        self._txtvar_key = tk.StringVar()
        self._txtvar_name = tk.StringVar()
        self._txtvar_type = tk.StringVar()
        self._txtvar_setting = tk.StringVar()
        self._txtvar_pathin = tk.StringVar()
        self._txtvar_pathout = tk.StringVar()
        pass
    def _showVars(self, key, data):
        self._txtvar_key.set(key)
        self._txtvar_name.set(self._getJsonVar(data, 'title'))
        self._txtvar_type.set(self._getJsonVar(data, 'type'))
        self._txtvar_setting.set(self._getJsonVar(data, 'path_setting'))
        self._txtvar_pathin.set(self._getJsonVar(data, 'path_in'))
        self._txtvar_pathout.set(self._getJsonVar(data, 'path_out'))
        pass
    def _getJsonVar(self, data, key):
        return key in data and data[key] or ''
    def _getTxtVar(self, var):
        tup = var.get()
        return tup and tup.strip() or ''
    def _setVars(self, key):
        if not self._checkInputs():
            return
        data = self._ini_json[key] = {}
        data['title'] = self._getTxtVar(self._txtvar_name)
        data['type'] = self._getTxtVar(self._txtvar_type)
        data['path_setting'] = self._getTxtVar(self._txtvar_setting)
        data['path_in'] = self._getTxtVar(self._txtvar_pathin)
        data['path_out'] = self._getTxtVar(self._txtvar_pathout)
        pass
    def _checkInputs(self):
        proj_key = self._getTxtVar(self._txtvar_key)
        proj_name = self._getTxtVar(self._txtvar_name)
        path_set = self._getTxtVar(self._txtvar_setting)
        path_in = self._getTxtVar(self._txtvar_pathin)
        path_out = self._getTxtVar(self._txtvar_pathout)
        return self._checkStr(proj_key) and self._checkStr(proj_name) and self._checkFile(path_set) and self._checkDir(path_in) and self._checkDir(path_out)

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class MainExport(MainInputVar):
    # -------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(MainExport, self).__init__(*args, **kwargs)
        pass
    # -------------------------------------------------
    def _exportFile(self, out_type):
        if not self._checkInputs():
            return
        parser = self._getExportParser(self._txtvar_type.get())
        if parser:
            # todo out_type
            parser.parseSettingXml(self._txtvar_setting.get())
            parser.exportFiles(self._txtvar_pathin.get(), self._txtvar_pathout.get())
            pass
        pass

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------


class MainUI(MainExport):
    _tk_listbox = None  # 左侧列表类
    # -------------------------------------------------
    def __init__(self, *args, **kwargs):
        super(MainUI, self).__init__(*args, **kwargs)
        self._renderUI(900, 600, 260, 400)
        self.log('初始化成功！')
        pass
    # -------------------------------------------------
    def _renderUI(self, width, height, list_width, list_height):
        height_t_ = height - list_height
        width_br_ = width - list_width
        row_br_ = width_br_ - 40
        self.setTitle('配置表工具')
        self.setSize(width, height)
        self.setResizable(0, 0)
        frm_t_ = tkFrame.getFrameTop(self._window, height_t_)
        frm_b_ = tkFrame.getFrameBottom(self._window, list_height)
        frm_bl_ = tkFrame.getFrameLeft(frm_b_, list_width)
        frm_br_ = tkFrame.getFrameRight(frm_b_, width - list_width)
        self._tk_txt_log = tkText.putScrollTextView(frm_t_, width)
        self._tk_listbox = tkListbox.putScrollListbox(frm_bl_, self._onEvtListBox)
        tkFrame.putFrameRowInput(frm_br_, row_br_, '选项', self._txtvar_key)
        tkFrame.putFrameRowInput(frm_br_, row_br_, '项目描述', self._txtvar_name)
        tkFrame.putFrameRowCombobox(frm_br_, row_br_, '输入类型', self._txtvar_type, ('excel', 'xml'))
        tkFrame.putFrameRowInput(frm_br_, row_br_, '项目配置文件', self._txtvar_setting, '打开', self._onEvtOpenDir, True)
        tkFrame.putFrameRowInput(frm_br_, row_br_, '输入目录', self._txtvar_pathin, '打开', self._onEvtOpenDir, False)
        tkFrame.putFrameRowInput(frm_br_, row_br_, '输出目录', self._txtvar_pathout, '打开', self._onEvtOpenDir, False)
        tkFrame.putFrameRowLine(frm_br_, row_br_)
        tkFrame.putFrameRowBtns(frm_br_, ['添加', self._onEvtAdd], ['删除', self._onEvtDel], ['保存', self._onEvtSave])
        tkFrame.putFrameRowLine(frm_br_, row_br_)
        tkFrame.putFrameRowBtns(frm_br_, ['导出json', self._onEvtExportJson])
        tkMenu.setMenuTopCmds(self._window, ['帮助', ['关于', self._onEvtAbout]])
        pass
    # -------------------------------------------------
    # events
    def _onEvtListBox(self, idx, key):
        self._showVars(key, self._ini_json[key])
        pass
    def _onEvtAbout(self):
        tkMessage.showMsgInfo(u'邮箱：alencai1990@foxmail.com', '联系方式')
        pass
    def _onEvtOpenDir(self, value, isFile):
        if isFile and value:
            value = os.path.dirname(value)
        if self._checkDir(value):
            excSys('start "" %s' % (value))
        pass
    def _onEvtAdd(self):
        try:
            key = self._getTxtVar(self._txtvar_key)
            assert (key.strip() != ''), ('Error: Empty key.')
            assert (not key in self._ini_json), ('Error: Already has key: %s' % key)
            self._setVars(key)
            self._writeIniParser()
            self.insertListKey(key)
        except Exception as e:
            self.error(e)
        pass
    def _onEvtDel(self):
        try:
            key = self._getTxtVar(self._txtvar_key)
            assert (key.strip() != ''), ('Error: Empty key.')
            assert (key in self._ini_json), ('Error: cant not find key.')
            self._ini_json.pop(key)
            self._writeIniParser()
            self.selectListFirst()
        except Exception as e:
            self.error(e)
        pass
    def _onEvtSave(self):
        try:
            key = self._getTxtVar(self._txtvar_key)
            assert (key.strip() != ''), ('Error: Empty key.')
            self._setVars(key)
            self._writeIniParser()
        except Exception as e:
            self.error(e)
        pass
    def _onEvtExportJson(self):
        self._exportFile('json')
        pass
    # -------------------------------------------------
    # apis: 
    def clearList(self):
        self._tk_listbox.delete(0, self._tk_listbox.size())
        pass
    def insertListKey(self, key):
        self._tk_listbox.insert(tk.END, key)
        pass
    def insertsList(self, arritems):
        for key in arritems:
            self._tk_listbox.insert(tk.END, key)
        pass
    def selectListFirst(self):
        keys = self._ini_json.keys()
        if len(keys) > 0:
            self._tk_listbox.selection_set(0)
            self._showVars(keys[0], self._ini_json[keys[0]])
        pass
    def refreshList(self):
        self.clearList()
        self.insertsList(self._ini_json.keys())
        self.selectListFirst()
        pass



