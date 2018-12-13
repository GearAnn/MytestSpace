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

# 写一个阶乘的函数 f(x)= x!，写出f
def fat(n):
    ret = 1
    for i in range(1, n+1):
        ret = ret * i
    return ret
print(fat(20))


# 现在用递归函数来实现此功能，但是递归效率很低，好处是代码短
# 递归函数的构造条件：1.可以自己调用自己  2.需要个结束条件
# 但凡是递归可以写的程序循环都可以解决
def fact(n):
    if n == 1:   # 结束条件
        return 1
    return n*fact(n-1)  # 体现了 fact(n)=n * fact(n-1)
print(fact(5))


# 写菲布拉切数列
# 0 1 1 2 3 5 8 13 21 34 55
# f(8)= f(7) + f(6)
#
def fibo(n):
    before = 0
    after = 1
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fibo(n-1) + fibo(n-2)  # 用f(8)= f(7) + f(6)来启发
print(fibo(10))






