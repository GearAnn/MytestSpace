#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: 线程同步锁.py
@time: 2018/9/5 0005 下午 4:51
"""

"""
需求：定义一个函数等于100，让它每次减1，用for循环需要减100次才可以减到0。但是这样太慢了！！
     为了提速，我们可以开100个进程，就可以一瞬间 就得到0。
"""
# 可以这样做：
import threading
import time
num = 100


def addNum():
    global num  # 每个线程都获取这个全局变量

    num -= 1    # 即addNum 就作一个 100 减 1的操作

    # FIXME 但是如果这里 把减一的过程复杂化(也达到100减1的效果):
    # temp = num + 1
    # num = temp - 2


"""
这样就容易造成，当temp = num + 1 执行完的时候 CPU 就切换了，并没有执行 num = temp - 2
等CPU再次切换回来的时候，num 并没有跟上一个执行线程的num数据进行同步，还是保持了自身原来的num数据
所以就形成了，线程之间信息不同步，线程之间不安全的现象，所以需要加入 同步锁！（也是GIL存在的意义）

更甚至：在python最初的版本上 'num -= 1'  这一行代码 都没有执行完 CPU就进行了切换，所以 final num 更不唯一
"""

thread_list = []

for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()   # 等待所有线程执行完成

print('final num', num)  # final num 0


"""
为了解决代码还没有执行完CPU就进行了切换导致线程之间数据不同步的问题，就需要人为的进行加锁阻塞
但是 如果用 join 就会把整个线程给阻塞住，造成串行，失去了多线程的意义，而我们要求把计算的步奏进行串行
这时就引出了 同步锁  来解决此类问题，其实在所有的编程语言中，为了保持数据的同步最简单的都是加锁。

加锁的格式：

lock = threading.Lock()

lock.acquire()
...算法...
lock.release()

这样用锁就把算法前后锁住，把算法这一段变成串行

"""

num = 100


def addNum():
    global num

    lock.acquire()
    temp = num
    time.sleep(0.00001)  # 如果不加锁 sleep会停止代码，让后面线程执行，但是num并没有被赋值，结果都是99
    num = temp - 1
    lock.release()   # 锁就是锁的这一段算法，其他的还是多线程，跟join阻塞整个线程有本质区别


lock = threading.Lock()
thread_list = []

for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()

print('final num', num)


# FIXME  重要问题：GIL已经在解释器上加锁了，但为什么代码中还需要锁
# FIXME  答案：GIL保证了同一时间只有一个线程进入解释器，而同步锁是保证了CPU不在代码执行的过程中进行切换
