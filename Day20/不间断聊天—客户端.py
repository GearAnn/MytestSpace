#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 不间断聊天—客户端.py.py
@time: 2018/8/28 0028 下午 6:39
"""

import socket


sk = socket.socket()

address = ('127.0.0.1', 8001)

sk.connect(address)

while True:

    inp = input('>>>')    # 切记：客户端和服务端双方，一接一发，一发一接，一一对应
    # if inp == 'exit':     # 可以这里加个判断条件来关闭对话
    #     break             # 注意！！当客户端单方关闭时，服务端收到的信息为空，此时服务端还需对应的进行关闭
    sk.send(bytes(inp, 'utf8'))

    data = sk.recv(1024)
    print(str(data, 'utf8'))


