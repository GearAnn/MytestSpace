#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 线程详解.py
@time: 2018/8/11 0011 下午 10:10
"""

"""
对于操作系统而言，一个任务就是一个进程
进程是系统中任务执行和资源分配的基本单位。每个进程都有自己的数据段、代码段、堆栈段
"""
"""
首先导入线程库(threading),
首先导入模块threading，通过threading.Thread()创建线程
其中target接收的是要执行的函数名字，args接收传入函数的参数，以元组（）的形式表示。
线程的调用函数格式：threading.Thread(target=foo, args=(1,)) 
"""
import time
import threading

def foo(n):
    print('foo%s' % n)  # 格式化输出
    time.sleep(1)

def bar(n):
    print('bar%s' % n)
    time.sleep(2)

# 创建2个子线程对象,t1,t2
# target 后面的就是你要处理函数的名字
# 其中target接收的是要执行的函数名字，args接收传入函数的参数，以元组（）的形式表示。
t1 = threading.Thread(target=foo, args=(1,))  # 执行t1
t2 = threading.Thread(target=bar, args=(2,))  # 执行t2
t1.start()  #  启动t1线程
t2.start()  #  启动t2线程
print('.....in the main.....')