#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: IO多路复用实现聊天.py.py
@time: 2018/10/24 0024 下午 10:06
"""

'''
之前学过，可以用socketsever和多线程来实现多人的聊天。这里使用IO多路复用来实现。
'''

# client


import time, socket


sk = socket.socket()
sk.connect(('127.0.0.1', 8800))
while True:

    inp = input(">>>")
    sk.sendall(bytes('hello', 'utf8'))
    data = sk.recv(1024)
    print(data.decode('utf8'))