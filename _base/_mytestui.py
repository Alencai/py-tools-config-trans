#!/usr/bin/python
# -*- coding: utf-8 -*-  
 
import os, sys
import random

# -------------------------------------------------

from _base._static import *
from _base._str import *

# -------------------------------------------------

if IS_PY2: 
    import Tkinter as tk
    import tkMessageBox
    import ttk
else:
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
    from tkinter import ttk

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

class MyBaseUI(object):
    _window = None

    # -------------------------------------------------

    # def __new__(cls, *args, **kwargs):
    #     # return xxxxx
    
    def __init__(self, *args, **kwargs):
        # super传入的类，必须最终继承于object才有效
        super(MyBaseUI, self).__init__(*args, **kwargs)
        self._window = tk.Tk(**kwargs)

    # -------------------------------------------------
    # api:

    def setTitle(self, title):
        if self._window:
            self._window.title(title)
    
    def setSize(self, width, height):
        if self._window:
            # self._window.resizable(0, 0) # 设置不可调整尺寸
            self._window.geometry(str(width) + 'x' + str(height))
            self._window.pack_slaves()

    def start(self):
        if self._window:
            self._window.mainloop()
    
    def exit(self):
        # if self._window:
        #     self._window.quit()
        sys.exit()
    
    # -------------------------------------------------

    def showMsgInfo(self, msg, title = 'msg'):
        tkMessageBox.showinfo(title=title, message=msg, parent=self._window)
        # return tkMessageBox.showerror(title=title, message=msg)
        # return tkMessageBox.showwarning(title=title, message=msg)
        
    def showMsgQues(self, msg, title = 'msg'):
        return tkMessageBox.askquestion(title=title, message=msg, parent=self._window)
        # return tkMessageBox.askyesno(title=title, message=msg)
        # return tkMessageBox.askokcancel(title=title, message=msg)

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

# https://www.cnblogs.com/shwee/p/9427975.html
# http://c.biancheng.net/python/tkinter/

class MyTestUI(MyBaseUI):
    _frame = None

    def __init__(self, *args, **kwargs):
        super(MyTestUI, self).__init__(*args, **kwargs)

    # -------------------------------------------------
    # helps:

    # pack: 
    # - anchor	当可用空间大于组件所需求的大小时，该选项决定组件被放置在容器的何处。该选项支持 N（北，代表上）、E（东，代表右）、S（南，代表下）、W（西，代表左）、NW（西北，代表左上）、NE（东北，代表右上）、SW（西南，代表左下）、SE（东南，代表右下）、CENTER（中，默认值）这些值。
    # - expand	该 bool 值指定当父容器增大时才是否拉伸组件。
    # - fill	设置组件是否沿水平或垂直方向填充。该选项支持 NONE、X、Y、BOTH 四个值，其中 NONE 表示不填充，BOTH 表示沿着两个方向填充。
    # - ipadx	指定组件在 x 方向（水平）上的内部留白（padding），默认为0。
    # - ipady	指定组件在 y 方向（水平）上的内部留白（padding），默认为0。
    # - padx	指定组件在 x 方向（水平）上与其他组件的间距，默认为0。
    # - pady	指定组件在 y 方向（水平）上与其他组件的间距，默认为0。
    # - side	设置组件的添加位置，可以设置为 TOP、BOTTOM、LEFT 或 RIGHT 这四个值的其中之一。
    def _helpPack(self):
        help(tk.Label.pack)

    # grid: 
    # - column	    指定将组件放入哪列，第一列的索引为 0。
    # - columnspan	指定组件横跨多少列。
    # - row	        指定组件放入哪行，第一行的索引为 0。
    # - rowspan 	指定组件横跨多少行。
    # - sticky	    类似 pack() 方法的 anchor 选项，同样支持 N（北，代表上）、E（东，代表右）、S（南，代表下）、W（西，代表左）、NW（西北，代表左上）、NE（东北，代表右上）、SW（西南，代表左下）、SE（东南，代表右下）、CENTER（中，默认值）这些值。
    def _helpGrid(self):
        help(tk.Label.grid)

    # place: 
    # - x	        指定组件的 X 坐标。x 为 0 代表位于最左边。
    # - y	        指定组件的 Y 坐标。y 为 0 代表位于最右边。
    # - relx	    指定组件的 X 坐标，以父容器总宽度为单位 1，该值应该在 0.0~1.0 之间，其中 0.0 代表位于窗口最左边，1.0 代表位于窗口最右边，0.5 代表位于窗口中间。
    # - rely	    指定组件的 Y 坐标，以父容器总高度为单位 1，该值应该在 0.0~1.0  之间，其中 0.0 代表位于窗口最上边，1.0 代表位于窗口最下边，0.5 代表位于窗口中间。
    # - width	    指定组件的宽度，以 pixel 为单位。
    # - height	    指定组件的高度，以 pixel 为单位。
    # - relwidth	指定组件的宽度，以父容器总宽度为单位 1，该值应该在 0.0~1.0 之间，其中 1.0 代表整个窗口宽度，0.5 代表窗口的一半宽度。
    # - relheight	指定组件的高度，以父容器总高度为单位 1，该值应该在 0.0~1.0 之间，其中 1.0 代表整个窗口高度，0.5 代表窗口的一半高度。
    # - bordermode  该属性支持“inside”或“outside” 属性值，用于指定当设置组件的宽度、高度时是否计算该组件的边框宽度。
    def _helpPlace(self):
        help(tk.Label.place)

    # -------------------------------------------------
    # render tests
    
    def _testLabel(self, parent):
        # label = tk.Label(parent, text='hello')
        # label.pack()
        txtvar = tk.StringVar()
        label = tk.Label(parent, textvariable=txtvar, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
        label.pack()
        txtvar.set('hello world')
    
    def _testBtn(self, parent):
        def btn_event():
            print("btn_event")
        btn = tk.Button(parent, text="hit me", font=('Arial', 12), width=10, height=1, command=btn_event)
        btn.pack()
    
    def _testEntry(self, parent):
        account = tk.Entry(parent, text="123", show=None, font=('Arial', 14))
        password = tk.Entry(parent, text="456", show='*', font=('Arial', 14)) 
        account.pack()
        password.pack()
        # text = account.get()

    def _testText(self, parent):
        txt = tk.Text(parent, height=3) # 这里hight是行数
        txt.pack()
        def text_insert(): # 在光标处插入
            txt.insert('insert', '_insert_') 
        def text_end():    # 在末位插入
            txt.insert('end', '_end_')
        tk.Button(parent, text="insert", command=text_insert).pack()
        tk.Button(parent, text="end", command=text_end).pack()
    
    def _testRadioBtn(self, parent):
        def radio_event():
            print("radio_event")
        txtvar = tk.StringVar()
        radio1 = tk.Radiobutton(parent, text='Option A', variable=txtvar, value='A', command=radio_event)
        radio2 = tk.Radiobutton(parent, text='Option B', variable=txtvar, value='B', command=radio_event)
        radio1.pack()
        radio2.pack()
    
    def _testCheckBtn(self, parent):
        def check_event():
            print("check_event")
        intvar1 = tk.IntVar()
        intvar2 = tk.IntVar()
        check1 = tk.Checkbutton(parent, text='Option A', variable=intvar1, onvalue=1, offvalue=0, command=check_event)
        check2 = tk.Checkbutton(parent, text='Option B', variable=intvar2, onvalue=1, offvalue=0, command=check_event)
        check1.pack()
        check2.pack()
    
    def _testComboBox(self, parent):
        cb = ttk.Combobox(parent, font=24)
        cb['values'] = ('Python', 'Swift', 'Kotlin')
        cb.pack(fill=tk.X, expand=tk.YES)

    def _testScale(self, parent):
        def print_scale(v):
            print("print_scale", v)
        scale = tk.Scale(parent, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_scale)
        scale.pack()
    
    def _testListBox(self, parent):
        frame = tk.Frame(parent, width=50)
        frame.pack()
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox = tk.Listbox(frame, height=5, yscrollcommand=scrollbar.set) # 这里的height是行数
        def on_select(evt):
            print(evt, listbox.curselection())
        listbox.bind('<ButtonRelease-1>', on_select)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        listbox.insert(tk.END, "a", "b", "c")
        for i in range(1, 5):
            listbox.insert(i, str(i))
        # listbox.delete(0, tk.END) # 删除所有
        scrollbar.config(command=listbox.yview)

    def _testCanvas(self, parent):
        canvas = tk.Canvas(parent, bg='green', height=100, width=100)
        image = tk.PhotoImage(file='./example/img.gif') 
        is_succ = canvas.create_image(100, 100, anchor=tk.CENTER, image=image)
        line = canvas.create_line(10, 10, 20, 20)  # 直线
        oval = canvas.create_oval(30, 30, 40, 40, fill='yellow')  # 圆
        arc = canvas.create_arc(40, 40, 70, 70, start=0, extent=180)  # 扇形
        rect = canvas.create_rectangle(70, 70, 80, 80)  # 矩形
        canvas.pack()
        def move_rect():
            canvas.move(rect, 2, 2)
        tk.Button(parent, text='move rect', command=move_rect).pack()

    def _testFrame(self, parent):
        frame1 = tk.Frame(parent)
        frame2 = tk.Frame(frame1)
        frame3 = tk.Frame(frame1)
        frame1.pack()
        frame2.pack(side='left')
        frame3.pack(side='right')
        tk.Label(frame1, text='frame', bg='red', font=('Arial', 16)).pack()
        tk.Label(frame2, text='frame_l', bg='green').pack()
        tk.Label(frame3, text='frame_r', bg='yellow').pack()
    
    def _testPack(self, parent):
        tk.Label(parent, text='P', fg='red').pack(side=tk.TOP)    
        tk.Label(parent, text='P', fg='red').pack(side=tk.BOTTOM) 
        tk.Label(parent, text='P', fg='red').pack(side=tk.LEFT)   
        tk.Label(parent, text='P', fg='red').pack(side=tk.RIGHT)  
    
    def _testGrid(self, parent):
        entry = tk.Entry(parent, relief=tk.SUNKEN, font=('Courier New', 24), width=18)
        entry.pack(side=tk.TOP, pady=10)
        frame = tk.Frame(parent)
        frame.pack(side=tk.TOP)
        names = "0123456789+-*/.="
        def btn_input(chr):
            entry.insert(tk.END, chr)
        for i in range(len(names)):
            btn = tk.Button(frame, text=names[i], font=('Verdana', 20), width=4, command=lambda chr=names[i]:btn_input(chr))
            btn.grid(row=i // 4, column=i % 4)

    # -------------------------------------------------

    def _testScrollBar(self, parent):
        # 坐标原点在左上角
        canvas = tk.Canvas(parent, scrollregion=(0, 0, 0, 2000))
        scroll = tk.Scrollbar(parent, orient=tk.VERTICAL)
        scroll.configure(command=canvas.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        frame = tk.Frame(canvas, width=100)
        canvas.config(yscrollcommand=scroll.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        def resize_frame(e):
            print("width=%d, height=%d" % (e.width, e.height)) # canvas['width']
            canvas.create_window(0, 0, anchor=tk.NW, window=frame, width=e.width) 
            canvas.unbind("<Configure>")
        canvas.bind("<Configure>", resize_frame)
        self._frame = frame
    
    # -------------------------------------------------
    # render menu

    # 第1级菜单
    def _testMenuBar(self, parent):
        menu = tk.Menu(parent)
        menu.add_cascade(labe='File', menu=self._testMenuFile(menu))
        menu.add_cascade(labe='Edit', menu=tk.Menu(menu, tearoff=0))
        parent.config(menu=menu)
    
    # 第2级菜单
    def _testMenuFile(self, parent):
        menu = tk.Menu(parent, tearoff = 0)
        menu.add_command(label='Add', command=self._onTestMenuEvt)
        menu.add_separator()
        menu.add_cascade(label='Sub', underline=0, menu=self._testMenuFileSub(menu))
        menu.add_separator()  
        menu.add_command(label='Exit', command=self.exit)
        return menu
    
    # 第3级菜单
    def _testMenuFileSub(self, parent):
        menu = tk.Menu(parent)
        menu.add_command(label='Sub1', command=self._onTestMenuEvt)
        menu.add_command(label='Sub2', command=self._onTestMenuEvt)
        return menu

    # empty event
    def _onTestMenuEvt(self, *args):
        print("evt empty job!")
    
    # -------------------------------------------------

    def randomColor(self):
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = "#"
        for i in range(6):
            color += nums[random.randint(0, len(nums) - 1)]
        return color

    def pushFrame(self):
        frame = tk.Frame(self._frame, bg=self.randomColor())
        frame.pack(fill=tk.X)
        sub = tk.Frame(frame)
        sub.pack(padx=10, pady=10)
        return sub

    def renderTests(self):
        self._testMenuBar(self._window)
        self._testScrollBar(self._window)
        self._testLabel(self.pushFrame())
        self._testBtn(self.pushFrame())
        self._testEntry(self.pushFrame())
        self._testText(self.pushFrame())
        self._testRadioBtn(self.pushFrame())
        self._testCheckBtn(self.pushFrame())
        self._testComboBox(self.pushFrame())
        self._testScale(self.pushFrame())
        self._testListBox(self.pushFrame())
        self._testCanvas(self.pushFrame())
        self._testFrame(self.pushFrame())
        self._testPack(self.pushFrame())
        self._testGrid(self.pushFrame())


