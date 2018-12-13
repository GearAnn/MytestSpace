#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 列表生成式.py
@time: 2018/8/13 0013 下午 9:35
"""
# 列表的数据是每一个都在内存里面

# 列表生成器   注意：这里不能 x for i,只能x for x 变量要对应
a = [x for x in range(1, 11)]  # 这是列表生成式：第一步取值用for,range，第二步列出计算方程
print(a)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 生成的值进行计算
a = [x*x for x in range(1, 11)]
print(a)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#  还可以把计算方程式定义成函数
def f(n):
    return n*n

a = [f(n) for n in range(1, 11)]  # 函数f(n)就是定义的计算方程式
print(a)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 赋值的简单形式
t = ('123', 8)

a, b = t  # 如果只有a=t/b=t则，a,b就是tuple,因为t有2个元素
          # 所以这里2个元素分别赋值给了a,b
print(a)
print(b)
a = t[0]  # 这是赋值的最开始的方式
b = t[1]
