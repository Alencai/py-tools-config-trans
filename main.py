#!/usr/bin/python
# -*- coding: utf-8 -*-  
 
import os, sys
from sys import version_info

# 配置数据
cf_file = 'config.ini'
cf_parser = None
name_url1 = 'url1'
name_url2 = 'url2'
name_url3 = 'url3'
list_sections = []
is_save_succ = False
is_py2 = False

# ui组件
rootWin = None
listBox = None
name = None
url1 = None
url2 = None
url3 = None

# -------------------------------------------------
# 兼容 py2 和 py3

if version_info.major == 2:
    import Tkinter
    import tkMessageBox
    import codecs
    import ConfigParser
    cf_parser = ConfigParser.ConfigParser()
    cf_parser.readfp(codecs.open(cf_file, 'r', 'utf-8-sig'))
    is_py2 = True
else:
    import tkinter as Tkinter
    import tkinter.messagebox as tkMessageBox
    import configparser
    cf_parser = configparser.ConfigParser()
    cf_parser.read(cf_file, encoding = 'utf-8-sig')


# -------------------------------------------------
# 配置表操作

def saveConfig():
    global is_save_succ
    is_save_succ = True
    section = name.get()
    if setSection(section):
        setOptionValue(section, name_url1, url1.get())
        setOptionValue(section, name_url2, url2.get())
        setOptionValue(section, name_url3, url3.get())
        cf_parser.write(open(cf_file, 'w'))

def deleteScetion():
    section = name.get()
    if setSection(section):
        cf_parser.remove_section(section)
        cf_parser.write(open(cf_file, 'w'))

def setSection(section):
    global is_save_succ
    if None == section:
        is_save_succ = False
        showInfo('项目名 不能为空')
        return False
    section = section.strip()
    if '' == section:
        is_save_succ = False
        showInfo('项目名 不能为空')
        return False
    if not cf_parser.has_section(section):
        cf_parser.add_section(section)
    return True

def setOptionValue(section, option, value):
    global is_save_succ
    if None == value or '' == value.strip():
        is_save_succ = False
        showInfo('目录 不能为空')
        return
    cf_parser.set(section, option, value)

def getOptionValue(section, option):
    if cf_parser.has_option(section, option):
        return cf_parser.get(section, option)
    return 'empty'

# -------------------------------------------------
# 以下是ui渲染

def renderFrameTop(parent):
    frame = Tkinter.Frame(parent)
    frame.pack()
    #
    global listBox
    scrollBar = Tkinter.Scrollbar(frame) 
    scrollBar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
    listBox = Tkinter.Listbox(frame, width=100, yscrollcommand=scrollBar.set)
    listBox.bind('<ButtonRelease-1>', onEvtSelectList)
    listBox.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)
    scrollBar.config(command=listBox.yview)
    
def renderFrameMid(parent):
    frame = Tkinter.Frame(parent)
    frame.pack()
    #
    global name, url1, url2, url3
    name = Tkinter.StringVar()
    url1 = Tkinter.StringVar()
    url2 = Tkinter.StringVar()
    url3 = Tkinter.StringVar()
    lbName = Tkinter.Label(frame, text='项目名', width=30)
    lb1 = Tkinter.Label(frame, text='excel目录', width=30)
    lb2 = Tkinter.Label(frame, text='excel索引文件', width=30)
    lb3 = Tkinter.Label(frame, text='xml目录', width=30)
    enyName = Tkinter.Entry(frame, textvariable=name, width=70)
    eny1 = Tkinter.Entry(frame, textvariable=url1, width=70)
    eny2 = Tkinter.Entry(frame, textvariable=url2, width=70)
    eny3 = Tkinter.Entry(frame, textvariable=url3, width=70)
    lbName.grid(row=1, column=1)
    lb1.grid(row=2, column=1)
    lb2.grid(row=3, column=1)
    lb3.grid(row=4, column=1)
    enyName.grid(row=1, column=2)
    eny1.grid(row=2, column=2)
    eny2.grid(row=3, column=2)
    eny3.grid(row=4, column=2)

def renderFrameBottom(parent):
    frame = Tkinter.Frame(parent)
    frame.pack()
    #
    btn1 = Tkinter.Button(frame, text='导出为js', command=onEvtSaveToJs, width=15)
    btn2 = Tkinter.Button(frame, text='导出为json', command=onEvtSaveToJson, width=15)
    btn3 = Tkinter.Button(frame, text='打开目录', command=onEvtOpenOutDir, width=15)
    btn4 = Tkinter.Button(frame, text='保存配置', command=onEvtAddSection, width=15)
    btn5 = Tkinter.Button(frame, text='删除配置', command=onEvtDeleteSection, width=15)
    btn1.grid(row=1, column=1)
    btn2.grid(row=1, column=2)
    btn3.grid(row=1, column=3)
    btn4.grid(row=1, column=4)
    btn5.grid(row=1, column=5)

def renderRoot():
    global rootWin
    rootWin = Tkinter.Tk()
    renderFrameTop(rootWin)
    renderFrameMid(rootWin)
    renderFrameBottom(rootWin)
    updateListItems()
    selectListItem(None)
    rootWin.mainloop()

def showInfo(msg):
    tkMessageBox.showinfo('提示', msg, parent=rootWin)

# -------------------------------------------------
# ui数据操作

def updateListItems():
    global list_sections
    list_sections = cf_parser.sections()
    listBox.delete(0, listBox.size())
    for section in list_sections:
        listBox.insert(Tkinter.END, section)

def selectListItem(section):
    if section is None and len(list_sections) > 0:
        section = list_sections[0]
    if cf_parser.has_section(section):
        name.set(section)
        url1.set(getOptionValue(section, name_url1))
        url2.set(getOptionValue(section, name_url2))
        url3.set(getOptionValue(section, name_url3))

# -------------------------------------------------
# 导出文件
import from_excel
import from_xml

def createDir(dir):
    print(dir)
    if os.path.exists(dir):
        return
    # os.mkdir(dir)  # 创建单个文件夹
    os.makedirs(dir)  # 创建多级文件夹

def saveToFile(xls_out_end, xls_str_dot, xml_out_pre, xml_out_end, xml_out_name, xml_str_dot, xml_str_newidn, xml_str_newline):
    # print(sys.path[0])
    # print(sys.argv[0])
    # print(os.getcwd())
    # print(os.path.abspath(__file__))
    # print(os.path.realpath(__file__))
    section = name.get()
    path = os.path.realpath('.')
    if is_py2:
        path = path.decode('GBK')
    path_tmp = path + '\\.tmp\\' + section + "\\"
    path_out = path + '\\.out\\' + section + "\\"
    if is_py2:
        createDir(path_tmp.encode('GBK'))
        createDir(path_out.encode('GBK'))
    else:
        createDir(path_tmp)
        createDir(path_out)
    #
    from_excel.in_excels = url1.get()
    from_excel.in_config = url2.get()
    from_excel.out_files = path_tmp
    from_excel.out_end = xls_out_end
    from_excel.str_dot = xls_str_dot
    from_excel.str_newidn = ""
    from_excel.str_newline = ""
    from_excel.write()
    #
    from_xml.in_xmls = url3.get()
    from_xml.in_files = path_tmp 
    from_xml.in_file_end = xls_out_end
    from_xml.out_pre = xml_out_pre
    from_xml.out_end = xml_out_end
    from_xml.out_file = path_out + xml_out_name
    from_xml.str_dot = xml_str_dot
    from_xml.str_newidn = xml_str_newidn
    from_xml.str_newline = xml_str_newline
    from_xml.write()

# -------------------------------------------------
# 以下是事件

def onEvtSelectList(evt):
    items = listBox.curselection()
    for itemIdx in items:
        selectListItem(listBox.get(itemIdx))

def onEvtAddSection():
    saveConfig()
    updateListItems()
    showInfo('保存成功')

def onEvtDeleteSection():
    deleteScetion()
    updateListItems()
    selectListItem(None)
    showInfo('删除成功')

def onEvtSaveToJs():
    print('onEvtSaveToJs')
    saveConfig()
    if is_save_succ:
        saveToFile("js", "", "module.exports=", ";", "flycfg.js", "", "", "")
        showInfo('导出成功')
    else:
        showInfo('导出失败')

def onEvtSaveToJson():
    print('onEvtSaveToJson')
    saveConfig()
    if is_save_succ:
        saveToFile("json", "\"", "", "", "flycfg.json", "\"", "    ", "\n")
        showInfo('导出成功')
    else:
        showInfo('导出失败')

def onEvtOpenOutDir():
    section = name.get()
    if setSection(section):
        path = os.path.realpath('.')
        if is_py2:
            path = path.decode('GBK')
        path_out = path + '\\.out\\' + section + "\\"
        if is_py2:
            path_out = path_out.encode('GBK')
        createDir(path_out)
        os.system("explorer " + path_out)
        return
    showInfo('打开目录失败')

# -------------------------------------------------

renderRoot()
