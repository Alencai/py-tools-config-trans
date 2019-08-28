#!/usr/bin/python
# -*- coding: utf-8 -*-  

from _mytk.tkHeaders import *

#-----------------------------------------------------------

# 图片全局缓存
_dictPhoto = {}
def __getPhotoImage(path):
    if not path in _dictPhoto:
        _dictPhoto[path] = tk.PhotoImage(file=path)
    return _dictPhoto[path]

#-----------------------------------------------------------

# 图片
def testRenderImage(canvas):
    img = __getPhotoImage('./assets/img.gif') # 必须存全局，否则会被释放，导致不显示
    img.configure(format='gif -index 0')    # gif 第0帧，可用定时器播放动画
    canvas.create_image(100, 100, anchor=tk.CENTER, image=img)

# 直线
def testRenderLine(canvas):
    canvas.create_line(10, 10, 20, 20)

# 圆
def testRenderOval(canvas):
    return canvas.create_oval(30, 30, 40, 40, fill='yellow')

# 扇形
def testRenderArc(canvas):
    return canvas.create_arc(40, 40, 70, 70, start=0, extent=180)

# 矩形
def testRenderRect(canvas):
    rect = canvas.create_rectangle(70, 70, 80, 80, fill='red')
    def move_rect(px, py, sx, sy):
        sx = (px < 0 or 190 < px) and -sx or sx 
        sy = (py < 0 or 190 < py) and -sy or sy 
        px += sx
        py += sy
        canvas.coords(rect, px, py, px + 10, py + 10)
        canvas.after(50, move_rect, px, py, sx, sy)
    move_rect(60, 70, 1, -1)
    return rect

def testCanvas(parent):
    canvas = tk.Canvas(parent, bg='green', height=200, width=200)
    testRenderImage(canvas)
    testRenderLine(canvas)
    testRenderOval(canvas)
    testRenderArc(canvas)
    testRenderRect(canvas)
    canvas.pack()

#-----------------------------------------------------------

