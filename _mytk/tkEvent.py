#!/usr/bin/python
# -*- coding: utf-8 -*-  


# <Button>	
#     某个鼠标按键在控件上被点击. detail 指定了哪一个按键被点击了, 比如, 
#         鼠标左键点击为 <Button-1>, 
#         鼠标中键点击为 <Button-2>, 
#         鼠标右键点击为 <Button-3>, 
#         向上滚动滑轮为 <Button-4>, 
#         向下滚动滑轮为 <Button-5>. 
#     如果在控件上按下鼠标的某个键并保持按下, Tkinter 将”抓住”该事件. 之后的鼠标事件, 比如,
#         鼠标移动 或 鼠标按键释放 事件, 会被自动发送给该控件处理, 即使鼠标移动出该控件时依然如此.
#     鼠标相对当前控件的位置会被存储在 event 对象中的 x 和 y 字段中传递给回调函数.
    
# <Motion>	
#     鼠标在某个按键被按下时的移动事件. 
#         鼠标左键点击为 <B1-Motion>, 
#         鼠标中键点击为 <B2-Motion>, 
#         鼠标右键点击为 <B3-Motion>. 
#     鼠标相对当前控件的位置会被存储在 event 对象中的 x 和 y 字段中传递给回调函数.

# <ButtonRelease>	
#     按钮点击释放事件. 
#         鼠标左键点击为 <ButtonRelease-1>, 
#         鼠标中键点击为 <ButtonRelease-2>, 
#         鼠标右键点击为 <ButtonRelease-3>. 
#     鼠标相对当前控件的位置会被存储在 event 对象中的 x 和 y 字段中传递给回调函数.

# <Double-Button>	
#     鼠标双击事件. 
#         鼠标左键点击为 <Double-Button-1>, 
#         鼠标中键点击为 <Double-Button-2>, 
#         鼠标右键点击为 <Double-Button-3>. 
#     Double 和 Triple 都可以被用作前缀. 
#     注意: 如果同时绑定单击事件 (<Button-1>) 和双击事件 (<Double-Button-1>), 则两个回调都会被调用.

# <Enter>	
#     鼠标移入控件事件. 
#     注意: 这个事件不是 Enter 键按下事件, 
#     Enter 按下事件是 <Return>.

# <Leave>	
#     鼠标移出控件事件.

# <FocusIn>	
#     控件或控件的子空间获得键盘焦点.

# <FocusOut>	
#     控件丢失键盘焦点 (焦点移动到另一个控件).

# <Return>	
#     Enter 点击事件. 
#     键盘上的所有键位都可以被绑定. 
#     特殊键位名称包括: 
#         Cancel, BackSpace, Tab, Return (Enter), Shift_L (任意 Shift), Control_L (任意 Control), Alt_L (任意 Alt), Pause, Caps_Lock, Escape, Prior (Page Up), Next (Page Down), End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock, and Scroll_Lock

# <Key>	
#     键盘按键点击事件. 
#     键值被存储在 event 对象中传递. (特殊键位会传递空键值).
#      “a” 键被点击. 其他字符也可以如此定义. 特殊情况包括 空格 (<space>) 和 小于号 (<less>). 
#     注意 “1” 是绑定键盘键位, 而 <1> 则是按钮绑定.

# <Shift-Up>
#     在 shift 被按下时点击 up 键. 
#     同样的, 也有 Alt-Up, Control-Up 事件.

# <Configure>	
#     控件大小改变事件. 
#     新的控件大小会存储在 event 对象中的 width 和 height 属性传递. 
#     有些平台上该事件也可能代表控件位置改变.


