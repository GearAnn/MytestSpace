#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: 进程之间的通信1.py
@time: 2018/10/10 0010 下午 7:02
"""

# 进程之间的通信大多数使用Pipe，Queue来实现，但是queue有区别，就是进程和线程的queue之间的区别

# FIXME 先讲用 Queue 来实现
"""
下列代码内容：
1.创建一个队列Queue
2.创建3个进程
3.每个进程的任务是往队列里面装数据
4.最后在主进程里面把数据取出来

运行会出现问题：  q.put([42, 2, 'hello']) 这里会报错， 原因是 q 不存在

因为 q=Queue()是在主进程里面创建的，但是在子进程里面没有创建，所以这里就体现了父子进程的通信不共享
"""
#
# from multiprocessing import Process, Queue
#
#
# def f():
#     q.put([42, 2, 'hello'])
#
#
# if __name__ == '__main__':
#     q = Queue()
#     p_list = []
#     for i in range(3):
#         p = Process(target=f)
#         p_list.append(p)
#         p.start()
#     print(q.get())
#     print(q.get())
#     print(q.get())
#
#     for i in p_list:
#         i.join()

"""
所以需要解决的问题就是：让子进程拿到主进程里面的q=Queue()
实现方法：就是把主进程的q=Queue()作为参数传给子进程
"""
from multiprocessing import Process, Queue


def f(q):
    q.put([42, 2, 'hello'])


if __name__ == '__main__':
    q = Queue()
    p_list = []
    for i in range(3):
        p = Process(target=f, args=(q,))  # q 作为了参数传入给了创建的子进程
        p_list.append(p)
        p.start()
    print(q.get())
    print(q.get())
    print(q.get())

    for i in p_list:
        i.join()

"""
问题来了：主进程里面的q=Queue中的 q 和 子进程f中的q.put 中的 q 是不是同一个q?
答案：不是同一个q,而且copy出来的另外一个q,验证这个观点只需要打印一下q的内存地址就OK了
"""


def f(q):
    q.put([42, 2, 'hello'])
    print("subprocess q:", id(q))  # 打印子进程的 q 内存ID


if __name__ == '__main__':
    q = Queue()
    print("mainprocess q:", id(q))  # 打印主进程的 q 内存ID
    p_list = []
    for i in range(3):
        p = Process(target=f, args=(q,))  # q 作为了参数传入给了创建的子进程
        p_list.append(p)
        p.start()
    print(q.get())
    print(q.get())
    print(q.get())

    for i in p_list:
        i.join()
