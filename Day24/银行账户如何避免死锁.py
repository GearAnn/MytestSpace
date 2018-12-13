#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: 银行账户如何避免死锁.py.py
@time: 2018/9/6 0006 上午 3:09
"""

"""
需求:创建一个银行账户，完成存取，显示余额，ID信息，转账的功能。

核心问题：
      
      1.会出现数据不同步的现象吗？
      
      2.会出现死锁的现象吗？？？

"""
import threading


class Account:
    def __init__(self, id, money):   # 把余额信息,id,封装到了Account里面
        self.id = id
        self.balance = money

    def withdraw(self, num):
        self.balance -= num

    def savemoney(self, num):
        self.balance += num


def transfer(self, to, count):  # 定义一个转帐功能，表明谁(self)向谁(to)转多少钱(count)
    self.withdraw(count)     # 转出方余额扣钱, 这里直接调用了withdraw方法，即余额扣钱
    to.savemoney(count)      # 转入方余额加钱，这里直接调用了savemoney方法，即余额加钱


a1 = Account('Alex', 1000)
a2 = Account('Xiaohu', 2000)

# 我们想开2个线程，让Alex给xiaohu转100，同时让xiaohu给Alex转200
t1 = threading.Thread(target=transfer, args=(a1, a2, 100))
t2 = threading.Thread(target=transfer, args=(a2, a1, 200))
# FIXME 重点：
"""
这时会出现一个现象，就是2个线程同时在走transfer,2个线程会同时拿到同一个balance,比如：
有2个账户同时给一个账户进行转账（2个线程同时走transfer），各转100，但是2个线程同时拿到的balance是1000
所以显示出来的余额是1100,但是应该是1200!
要点：有时不能让多个线程同时对同个数据进行修改！而是多个线程要同步上一个的线程的操作数据！

解决：这个时候为了保证数据的同步，就必须加锁。

方案有多种：

    1.可以对每一个操作数据的函数进行加锁，但是这个方法有个大前提！就是这几个函数是同一个操作对象，才能实现数据同步！
      但是如果不是同一个操作对象，如何解决？

    2.根本解决方案：在类里面加锁! 既在每一个单独操作数据的函数上加锁！但又要避免死锁的现象！

如下：
"""


class Account:
    def __init__(self, id, money):
        self.id = id
        self.balance = money

    def withdraw(self, num):
        r.acquire()           # 在每一个操作数据的函数上加锁！
        self.balance -= num
        r.release()

    def savemoney(self, num):
        r.acquire()           # 在每一个操作数据的函数上加锁！
        self.balance += num
        r.release()

    def other_op(self):   # 在里面还需要有其他调用函数的操作
        r.acquire()       # 在每一个操作数据的函数上加锁！
        # FIXME 核心：
        self.withdraw()   # 这里直接调用了withdraw,但是withdraw里面也有一把锁，就可能会造成里外相互死锁的现象
        r.release()       # 这个里就为了避免死锁！就体现了下面 r = threading.RLock() 的意义！


def transfer(self, to, count):
    self.withdraw(count)
    to.savemoney(count)


r = threading.RLock()   # 创建递归锁
a1 = Account('Alex', 1000)
a2 = Account('Xiaohu', 2000)
