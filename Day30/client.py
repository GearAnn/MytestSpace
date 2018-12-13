#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: client.py.py
@time: 2018/10/24 0024 下午 7:38
"""

"""
IO多路复用在socket中的应用

即：1个select可以监听多个socket对象
"""

import socket
import time


sk = socket.socket()

while True:
    sk.connect(('127.0.0.1', 6667))
    print('hello')
    sk.sendall(bytes('hello', 'utf8'))
    time.sleep(2)
    break
