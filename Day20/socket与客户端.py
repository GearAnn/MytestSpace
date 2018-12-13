#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: socket与客户端.py.py
@time: 2018/8/28 0028 下午 4:20
"""

# 服务端已经好了，等待客户端连接connect
# 注意：先开服务端，再开客户端

import socket


sk = socket.socket()

address = ('127.0.0.1', 8000)  # 服务端IP地址和端口

sk.connect(address)  # 到此连接成功，但是未进行通信，通信内容还要重新写

data = sk.recv(1024)  # 1024表示一次接收的数据量
# 客户端在建立连接时，把本地端口,本地socket,本地IP发给了服务端

print(data)  # 注意如果接收的是汉字则需要把byte类型转码， 使用 str(data,'utf8')






