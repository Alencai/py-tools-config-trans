#!/usr/bin/python
# -*- coding: utf-8 -*-  
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

#-----------------------------------------------------------

from _base import *

#-----------------------------------------------------------

import threading
if IS_PY3:
    from functools import reduce

#-----------------------------------------------------------

print('>>-----------------------------------------------')

# # 定时器
# def time_evt():
#     print('test')
#     threading.Timer(0.5, time_evt).start()
# time_evt()

print('>>-----------------------------------------------')

# 测试： range 、 enumerate 、 for 、 lambda

li_data1 = range(2)
# li_data1 = [0, 1]                           # 与上一样
# li_data1 = [i for i in range(2)]            # 与上一样
# li_data1 = [i for i in range(10) if i < 2]  # 与上一样
li_data2 = range(3, 10, 2)
en_data = enumerate(li_data1)
kv_data = {'a': 'apple', 'b': 'banana'}

print(li_data1)
print(li_data2)
print(en_data)
print(kv_data)

print('>>-----------------------------------------------')

for value in li_data1:
    print(value)

print('--------------------')

for key, value in en_data:
    print(key, value)
print('--------------------')

for key in kv_data: 
    print(key, kv_data.get(key))
# for key, value in kv_data.items():     # 与上一样
#     print(key, value)    
# for key, value in dict.items(kv_data): # 与上一样
#     print(key, value) 
    
print('>>-----------------------------------------------')

print('filter', filter(lambda x: x * x, range(5)))
print('map', map(lambda x, y: (x or 1) * (y or 1), range(5), range(6)))
print('reduce', reduce(lambda x, y: x + y, range(5)))  # 迭代，0+1+...+5

print('>>-----------------------------------------------')

fun1 = lambda:1
fun2 = lambda x, y: x + y
fun3 = lambda x, y: (x + y, x * y)
fun4 = [(lambda x, y=i: x + y) for i in range(3)]
print("--lambda 1. %d" % fun1())
print("--lambda 2. %d" % fun2(1, 2))
print("--lambda 3. %d %d" % fun3(2, 3)) # 返回多个参数
print("--lambda 4. %d" % fun4[1](4))

print('>>-----------------------------------------------')

# 星号(*/**)操作符

# 用于收集参数：
def test1(*args, **kwargs):
    print(args, kwargs)
test1(1, 2, 3, a=1, b=2, c=3)

print('--------------------')

# 用于解参数：
def test2(x, y, z, a, b, c):
    print(x, y, z, a, b, c)
args = [1, 2, 3]
kwargs = {'a': 1, 'b': 2, 'c': 3}
test2(*args, **kwargs)

print('--------------------')

# 奇怪的用法（复制dict）：
def test3(**kwargs):
    del kwargs['a'] # 删除一个元素，但不影响原来的
    return kwargs
kw1 = {'a': 1, 'b': 2, 'c': 3}
kw2 = test3(**kw1)
print(kw1, kw2)

print('>>-----------------------------------------------')

print(type(1), type(1.1), type('1'), type(False))
print(type([]), type({}), type((1, 2)))
print(type(test1), type(lambda:1))

print('>>-----------------------------------------------')


def print_str(txt):
    print(txt, type(txt))
    appendFile(txt, 'abc.txt')
txt = "1.用户\n2.用户\n3.用户"

txt2 = 'hello world'
print_str(txt2)
txt2 = enUTF8(txt2)
print_str(txt2)
txt2 = deUTF8(txt2)
print_str(txt2)
