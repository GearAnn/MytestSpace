#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: 进程之间的通信2.py
@time: 2018/10/10 0010 下午 7:51
"""

# FIXME 多进程之间的通信之Pipe的使用

from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])  # 子进程中发送信息
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  # 跟学习sever通信的内容一样，conn表示管道
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # 跟学习sever通信的内容一样，recv表示接收阻塞 （主进程收到子进程发送的信息）
    p.join()

"""
关键点：上面代码之所以主进程能收到子进程发送的信息，是因为parent_conn, child_conn = Pipe() 的存在，使得2者之间建立的通道
"""
