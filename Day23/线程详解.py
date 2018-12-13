#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: 线程详解.py
@time: 2018/9/3 0003 下午 8:10
"""

"""
Python中的在国际上的通用解释器是 Cpython

程序执行的过程：

                +------------+
                |   应用层    |
                +------------+
                      |
                      v
            +--------------------+
            |   解释器 Cpython    |
            +--------------------+
                      |
                      v
            +--------------------+
            |     OS 操作系统      |
            +--------------------+
                      |
                      v
+------------+   +------------+  +------------+
|    CPU     |   |    DISK    |  |    RAM     |
+------------+   +------------+  +------------+

什么是线程（thread）?
线程是OS能狗进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位。一条线程指的是进程中一个单一顺序的控制流，
一个线程就是一个指令集合，一个进程中可以并发多个线程，每个线程执行不同的任务。

什么是进程（process）?
对于操作系统而言，一个任务就是一个进程，一个进程可以有多个线程
进程是系统中任务执行和资源分配的基本单位。每个进程都有自己的数据段、代码段、堆栈段


"""

# FIXME 创建线程的基本方法

# 创建线程：
# 首先导入模块threading，通过threading.Thread()创建线程
# 其中target接收的是要执行的函数名字，args接收传入函数的参数，以元组（）的形式表示。
# 线程的调用函数格式：threading.Thread(target=foo, args=(1,))


import threading


def foo(n):
    print('foo%s' % n)


def bar(n):
    print('bar%s' % n)

# 创建 2个子线程,主线程为程序本身
# target= 表示要执行的函数名字


t1 = threading.Thread(target=foo, args=(1,))

t2 = threading.Thread(target=bar, args=(2,))

# 运行2个子线程
t1.start()  # foo1
t2.start()  # bar2


"""
注意：Python中多线程不一定比串行要快，甚至很多时候运算速度会慢一倍，原因有2个：

1.多线程没有io阻塞,CPU要花费资源去切换

2.就是GIL的存在

这里引出2个概念:

io密集型任务

计算密集型任务
(可以多核CPU来避免因为CPU切换来造成资源浪费,Java可以通过编程解决，Cpython中只能利用单核CPU,甚至就几乎等于Python是个单线程的程序)

"""

# FIXME 通过类来创建一个线程

# 步奏：
# 1.创建一个类class（等价于需要创建的线程）并继承 threading.Thread
# 2.把线程参数args放入 __init__
# 3.把需要定义的函数封装到 函数run里面去
# 4.用标准格式 if __name__=='main':
#   t1
#   t2
#   t1.start()
#   t2.start()

import time

# 第一步


class MyThread(threading.Thread):
    # 第二步:处理 args（实例化） ，即传入参数用 __init__去拿，把参数封装到了对象里面
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num  # 这是实例变量

    # 第三步:处理需要定义的函数，即自定义函数用 run(self) 来重写
    def run(self):    # run 是父类里面的函数，这里进行了重写，然后内部自动运行一次
        print('running on number:%s' % self.num)

        time.sleep(3)


if __name__ == '__main__':

    t1 = MyThread(1)    # (1) 就是 args=（1，），即传入的参数
    t2 = MyThread(2)    # (2) 就是 args=（2，），即传入的参数

    t1.start()  # running on number:1
    t2.start()
