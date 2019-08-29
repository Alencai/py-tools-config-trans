#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

def testListbox(parent):
    frame = tk.Frame(parent, width=50)
    frame.pack()
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox = tk.Listbox(frame, height=5, yscrollcommand=scrollbar.set) # 这里的height是行数
    def on_select(evt):
        idxs = listbox.curselection()
        print('testListBox: ', listbox.get(idxs[0]), idxs)
    listbox.bind('<ButtonRelease-1>', on_select)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)
    listbox.insert(tk.END, "a", "b", "c")
    for i in range(1, 5):
        listbox.insert(1, str(i))
    scrollbar.config(command=listbox.yview)
    tk.Button(parent, text='remove all', command=lambda:listbox.delete(0, tk.END)).pack()


#-----------------------------------------------------------

# 获取带滚动条的listbox
def putScrollListbox(parent, command):
    def click_evt(evt):
        for idx in evt.widget.curselection():
            return idx, evt.widget.get(idx)
        return -1, None
    scroll = tk.Scrollbar(parent) 
    listbox = tk.Listbox(parent, yscrollcommand=scroll.set)
    listbox.bind('<ButtonRelease-1>', lambda evt:command(*click_evt(evt)))
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
    scroll.config(command=listbox.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    return listbox





