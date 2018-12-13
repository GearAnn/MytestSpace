#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: 队列queue.py
@time: 2018/9/10 0010 下午 4:55
"""

"""
多线程利器：queue模块。

队列queue 是相当于一个列表 是放数据的列表，也是一个模块。

包含3个主要方法：

1.创建队列： q = queue.Queue()，可以在（）中加入数字，表示队列中可以包含的数据量,比如 d = queue.Queue(3)，包含3个数据
2.放入数据： q.put()
3.拿数据:   q.get()

queue如何解决多线程问题： 避免了多线程同时拿到一个list中的同一个数据的现象。

注意:
1.放入和拿出数据是先进现出 frist in frist out! 类似于堆栈！
2.如果队列中加入了数量限制，也可以无限的加入数据，但是多余的数据在后面排队，等列队中的数据出去后，后面的数据按顺序挤进队列
3.queue队列中自带了锁，确保了多线程的安全

queue还有其他查询方法：

q.qsize() : 返回列队大小
q.full()  : 判断队列是否满了
q.empty() : 判断是否为空
"""

import queue

d = queue.Queue()

d.put('Jin')
d.put('Xiao')
d.put('Hao')

print(d.get())
print(d.get())
print(d.get())
# frist in frist out
# Jin
# Xiao
# Hao

# 用吃包子的例子来示范queue的多线程用法
import threading
import queue
from time import sleep
from random import randint


class Production(threading.Thread):
    def run(self):
        while True:
            r = randint(0, 100)
            q.put(r)  # 往里面塞包子的时候 用queue就保证了先后顺序，不会同时塞同一个包子
            print("生产出来%s号包子" % r)
            sleep(1)


class Process(threading.Thread):
    def run(self):
        while True:
            re = q.get()
            print("吃掉%s号包子" % re)


if __name__ == "__main__":
    q = queue.Queue(10)
    threads = [Production(), Production(), Production(), Process()]
    for t in threads:
        t.start()
