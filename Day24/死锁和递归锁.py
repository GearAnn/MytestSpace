#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: 死锁和递归锁.py
@time: 2018/9/5 0005 下午 6:31
"""

# 死锁现象：
import threading
import time


class myThread(threading.Thread):
    def doA(self):
        lockA.acquire()
        print(self.name, 'gotlockA', time.ctime())
        time.sleep(3)
        lockB.acquire()
        print(self.name, 'gotlockB', time.ctime())
        lockB.release()
        lockA.release()

    def doB(self):
        lockB.acquire()
        print(self.name, 'gotlockB', time.ctime())
        time.sleep(2)
        lockA.acquire()
        print(self.name, 'gotlockA', time.ctime())
        lockA.release()
        lockB.release()

    def run(self):  # 5个线程同时执行run(同时执行doA,doB)
        self.doA()
        self.doB()


if __name__ == '__main__':

    lockA = threading.Lock()
    lockB = threading.Lock()
    threads = []
    for i in range(5):
        threads.append(myThread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()

# 运行结果会出现:即打印了第一个线程doA 和 doB 的前半段 ， 再打印了 第二个线程doA的前半段  就不往下走了
# Thread-1 gotlockA Wed Sep  5 18:45:42 2018
# Thread-1 gotlockB Wed Sep  5 18:45:45 2018
# Thread-1 gotlockB Wed Sep  5 18:45:45 2018
# Thread-2 gotlockA Wed Sep  5 18:45:45 2018
# 结局：doA占用了B锁但需要A锁，doB占用了A锁但需要B锁，造成了相互锁死的状态
# 解决方案：使用递归锁，即添加一把共用锁且可以重复使用

# 递归锁：threading.RLock()


class myThread(threading.Thread):
    def doA(self):
        lock.acquire()
        print(self.name, 'gotlockA', time.ctime())
        time.sleep(3)
        lock.acquire()
        print(self.name, 'gotlockB', time.ctime())
        lock.release()
        lock.release()

    def doB(self):
        lock.acquire()
        print(self.name, 'gotlockB', time.ctime())
        time.sleep(2)
        lock.acquire()
        print(self.name, 'gotlockA', time.ctime())
        lock.release()
        lock.release()

    def run(self):
        self.doA()
        self.doB()


if __name__ == '__main__':

    lock = threading.RLock()  #
    # lockA = threading.Lock()
    # lockB = threading.Lock()
    threads = []
    for i in range(5):
        threads.append(myThread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()


#  结论：这样用递归锁，即 2个函数共同同一个锁lock = threading.RLock()就可以避免死锁现象

