#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: 迭代器.py
@time: 2018/8/14 0014 上午 11:40
"""

# FIXME  生成器都是迭代器，迭代器不一定是生成器，生成器是特殊的迭代器
# FIXME  什么是迭代器：1满足 iter 方法，2满足 next 方法

"""
for in 循环函数 内部做的3个事情：
1.使用iter方法/调用可迭代对像，返回一个迭代器对象
2.不断调用迭代器对象的 next 方法
3.处理 next 的Stopiteration 异常
"""

l = [1, 2, 3, 4]
d = iter(l)  # l是个list 是个可迭代对象
print(d)  # <list_iterator object at 0x0000000001D55A58>
# 因为list dict都是可迭代对象，所以都可以调用 next()
print(next(d))  # 1
print(next(d))  # 2
print(next(d))  # 3
print(next(d))  # 4



# 判断对象是不是可迭代，导入函数库


from collections import Iterable,Iterator


s = [1, 2, 3]
a = iter(s)
isinstance(s, list)
print(isinstance(s, list))  # True
print(isinstance(s, Iterator))  # False
print(isinstance(s, Iterable))  # s 只是可迭代对象
print(isinstance(a, Iterator))  # a 才是迭代器
print(a)  # <list_iterator object at 0x0000000002113358>

# FIXME 凡是可以用for in循环的对象和可用next()的都是Iterable类型
# FIXME list dict str 都是Iterable类型，但是不是Iterator(迭代器)，但是可以通过iter()转为迭代器

# 比如以后要打开一个文档，并不需要把整个文档放下内存，迭代器就可以把文档的每一行当做元素放入内存
with open('adc.txt') as f:   # 这里 f 就是个Iterable,for in循环自动把f转为了Iterator
    for i in f.readlines():  # f.readlines 是把文档的每一行当做元素依次提取
        print(i)             # 因为是可迭代，所以内存里面永远只有一行的内容


# 使用文件读取 ，找出最长的一行？
a = max(len(x.strip()) for x in open('adc.txt', 'r'))
print(a)
#  第二种方法
txt = open('adc.txt', 'r')
words = txt.readlines()
print(max(words))

