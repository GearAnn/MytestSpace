#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: gevent实现的协程.py
@time: 2018/10/18 0018 上午 12:49
"""

"""
Gevent是一个第三方库，可以轻松的通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是Greenlet,它是以C扩展模块形式接入Python的
轻量级协程。Greenlet全部运行在主程序操作系统进程的内部，但被协作式调度。
"""

import gevent, time


def foo():
    print('Running in foo', time.ctime())
    gevent.sleep(1)  # sleep在这里模拟一个IO阻塞的情况
    print('Explicit context switch to foo again')


def bar():
    print('Explicit context to bar', time.ctime())
    gevent.sleep(2)  # 当上面gevent.sleep的时候，线程会自动切换并执行到这里
    print('Implici context switch back to bar')


gevent.joinall([gevent.spawn(foo), gevent.spawn(bar)])

"""
以上代码的用协程的意义：因为是一个串行，如果用gevent这样就可以节约出1S的时间，而不是从上到下的3S总时间。
注意：gevent.sleep()与time.sleep（）的不同在于，gevent.sleep()是在同一线程下的切换，而time.sleep()
     是CPU之间的切换。
"""



# greenlet的switch方法
from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
print(gr1)  # <greenlet.greenlet object at 0x00000000023E38D0> gr1 就是一个greenlet对象
gr2 = greenlet(test2)
print(gr2)  # <greenlet.greenlet object at 0x00000000023E38D0> gr2 就是一个greenlet对象

# FIXME greenlet对象就用switch方法来完成不同任务之间的来回切换
gr1.switch()
# 返回
# 12
# 56
# 34
# 78

# FIXME 因为gr1用switch调用的时候，执行的是test1,print(12)后，执行gr2.switch(),就切换到了gr2用switch来调用并执行test2
