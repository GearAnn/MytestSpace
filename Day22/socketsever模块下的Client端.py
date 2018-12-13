#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: socketsever模块下的Client端.py
@time: 2018/9/3 0003 下午 6:24
"""


import socket


sk = socket.socket()

address = ('127.0.0.1', 8099)

sk.connect(address)
print('客户端启动..')

while True:

    inp = input('>>>')
    sk.send(bytes(inp, 'utf8'))

    data = sk.recv(1024)
    print(str(data, 'utf8'))
