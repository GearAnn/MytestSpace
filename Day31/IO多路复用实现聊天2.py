#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: IO多路复用实现聊天2.py.py
@time: 2018/10/25 0025 下午 7:47
"""

# sever


import socket
import select


sk = socket.socket()

sk.bind(('127.0.0.1', 8800))
sk.listen()

inp = [sk, ]

while True:
    # FIXME 重点 为什么要secelt监听con不能直接监听sk
    inputs, outputs, error = select.select(inp, [], [], )

    for obj in inputs:  # [conn]
        if obj == sk:
            conn, addr = sk.accept()
            #FIXME 注意：IO模型的第二步给内核发送拷贝数据的recvfrom这个系统调用，这里由accept发出
            print(conn)
            inp.append(conn)  # 注意这里新添加的conn是独立的，不会同一个通道，是各自的通道

        else:
            data = conn.recv(1024)
            print(data.decode('utf8'))
            Inputs = input("回答>>>" % inp.index(obj))
            obj.sendall(Inputs.encode('utf8'))
