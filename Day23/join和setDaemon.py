#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: join和setDaemon.py.
@time: 2018/9/5 0005 上午 10:15
"""

"""
xx.join()  表示阻塞的意思，xx.join以上的代码执行完了在执行以下的代码
"""


import time
import threading


def a(n):
    print('%s' % n)
    time.sleep(3)


def b(n):
    print('%s' % n)
    time.sleep(2)


t1 = threading.Thread(target=a, args=(1,))
t2 = threading.Thread(target=b, args=(2,))

begin = time.time()

t1.start()
t1.join()  # 这里就阻塞住了，等a停3S后再继续走

t2.start()

end = time.time()

print(begin - end)


"""
线程中的3个重要参数： 

一：
t1.setDaemon(True)

t1.setDaemon(True)表示守护线程t1，当主线程运行完后需要等待子线程时，如果在子线程后加入 t1.setDaemon(True) 则主线程执行完后整个程序就结束。

注意：如果t1守护了，但是t2没有守护，则还是需要等t2只是t1不能再等.


二：
print(threading.current_thread())  ：可以显示当前运行的线程

三：
print(threading.active_count())   : 可以显示当前还在运行的线程数量

注意：当线程执行结束后，则不算入当前运行的线程数量。
 

"""




