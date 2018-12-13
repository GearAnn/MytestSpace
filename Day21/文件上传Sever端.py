#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 文件上传Sever端.py.py
@time: 2018/9/2 0002 下午 10:46
"""

"""
目的：把Client端的‘QQ图片.jpg’上传一个文件到Sever端中名为‘文件接收’文件夹里

"""
import socket
import os

sk = socket.socket()

address = ('127.0.0.1', 8010)

sk.bind(address)

sk.listen(3)

print('waitting.....')

# 拿到路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


conn, addr = sk.accept()

while True:

    conn, addr = sk.accept()   # 一个客户端关闭后，利用while循环继续连接其他服务端

    while True:
        data = conn.recv(1024)
        # 接收方也要解析文件
        cmd, file_name, file_size = str(data, 'utf8').split('|')
        # 路径拼接
        path = os.path.join(BASE_DIR, '文件接收', file_name)
        # file_size 是 str类型，转化为int类型
        file_size = int(file_size)

        f = open(path, 'ab')

        # 文件循环发过来了，所以需要循环接收,同样需要加条件来限制循环
        has_receive = 0
        while has_receive != file_size:
            data = conn.recv(1024)
            f.write(data)
            has_receive += len(data)






