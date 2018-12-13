#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 不间断聊天—服务端.py.py
@time: 2018/8/28 0028 下午 6:38
"""

# 建立不间断聊天就一接一发，一发一接，之上加上while Ture循环就可以了


import socket


sk = socket.socket()

address = ('127.0.0.1', 8001)

sk.bind(address)

sk.listen(3)

print('waitting.....')

conn, addr = sk.accept()

while True:

    data = conn.recv(1024)      # 切记：客户端和服务端双方，一接一发，一发一接，一一对应
    # if not data:           # if not data 对应的服务端单方关闭时发送的空信息
    #     break              # 但是在服务器一般情况下是不能关闭
    print(str(data, 'utf8'))

    inp = input('>>>')
    conn.send(bytes(inp, 'utf8'))






