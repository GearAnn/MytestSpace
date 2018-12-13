#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 递归函数.py
@time: 2018/8/12 0012 下午 10:10
"""

# eval 可以把字符串转换为字典,也有简单计算值的功能
print(eval('1+2+3'))  # 直接求值 6

# filter（func,str）有2个参数，第一个参数放函数(匹配条件)，第二个参数放列表
# filter就是判断列表里的每一个元素，把他们传入到函数里面
str = ['a', 'b', 'c', 'd']

def fun1(s):      # 这就是定义的函数，代表过滤条件
    if s != 'a':  # 把str里的元素传入，然后返回该元素
        return s

ret = filter(fun1, str)  # 把str里的元素，传入fun1（过滤条件）
#  (b','c','d') 返回的就是过滤掉的
print(ret)   # # ret是一个迭代器,迭代器相当于一个容器,里面的内容不在占内存空间
print(list(ret))  # 所以显示出迭代器里的内容，要把它先调用成 list/dict.py 类型


# map函数,可以对元素进行一个修改，修改内容只取决与函数
str = ['d', 'a', 'd']

def fun2(s):
    return s + 'alvin'  # 这个函数和map共同就把传入值给修改

ret = map(fun2, str)  # 如果这里使用filter则条件不起任何作用，因为filter只过滤不修改
print(ret)
print(list(ret))  # ['dalvin', 'aalvin', 'dalvin']


# reduce 需要导入functools模块
# reduce 代表从左到右依次把list前2个元素求和。
from functools import reduce
list = [1,2,3,4,5]  # 前2个元素求和为：[3,3,4,5] -> [6,4,5]-> [10,5] -> 15
def add1(x, y):
    return x + y

print(reduce(add1, list)) # reduce直接返回值 15


# 非匿名函数
def add(a, b):
    return a + b  # 这个函数的名字就是 add ,不是匿名的

# lambda匿名函数,就是没有名字，格式： lambda 后面直接跟表达式，参数 ,适合简单函数
# 也叫函数式编程，跟面向对象的编程有差异
sum = lambda x,y: x + y,range(1,6)  # 这就是lambda匿名函数的格式,后面直接跟表达式,参数
# 通过reduce和lambda表达式实现阶乘
print(reduce(lambda x, y: x * y, range(1, 6)))  # 120









