#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 程序传输Sever端.py.py
@time: 2018/8/29 0029 下午 5:44
"""

"""
目的：

给对方传送一个程序命令，让对方执行，然后让对方把执行后的结果返回过来。

"""

# FIXME Sever端

import subprocess


import socket


sk = socket.socket()

address = ('127.0.0.1', 8005)

sk.bind(address)

sk.listen(3)

print('waitting.....')

conn, addr = sk.accept()

while True:

    conn, addr = sk.accept()   # 一个客户端关闭后，利用while循环继续连接其他服务端

    while True:

        data = conn.recv(1024)  # 以下4行就这一句是核心，目的就是拿到data,其他都是附加条件
        if not data:
            break
        print(str(data, 'utf8'))

        # 核心问题：拿到了data(就是client发来的命令程序),如何执行data？ 这时需要用 subprocess
        obj = subprocess.Popen(str(data, 'utf8'), shell=True, stdout=subprocess.PIPE)
        # 注意data信息类型的转化
        cmd_result = obj.stdout.read()  # data执行结果封装进了obj,然后obj进行调用

        conn.send(cmd_result)

