#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 文件上传Client端.py.py
@time: 2018/9/2 0002 下午 10:46
"""

"""
目的：把Client端的‘QQ图片.jpg’上传一个文件到Sever端中名为‘文件接收’文件夹里

主要步骤:
  1.找出文件路径
  2.统一和取出文件名字
  3.告诉对方文件大小
  4.打包所有的信息，然后传送过来

"""

import socket
import os

sk = socket.socket()

address = ('127.0.0.1', 8010)

sk.connect(address)

# FIXME QQ图片.jpg是当前文件夹的路径，还需要绝对路径,然后解析图片

BASE_DIR = os.path.dirname(os.path.abspath(__file__))



while True:

    inp = input('>>>').strip()  # post QQ.jpg

    cmd, path = inp.split('|')

    # 拼接路径用 os.path.join
    path = os.path.join(BASE_DIR, path)

    # os.path.basename(path) 就是在()中放下参数路径，就可以取到参数的名字
    # 取名字的目的就是告诉Sever端，文件的名字需要统一
    file_name = os.path.basename(path)

    # 取文件大小，告诉Sever端文件接收的大小
    file_size = os.stat(path).st_size

    # 打包需要传输的信息
    file_info = 'post|%s|%s' % (file_name, file_size)

    sk.sendall(bytes(file_info, 'utf8'))

    # 现在读取文件，并上传文件
    f = open(path, 'rb')
    has_send = 0  # 因为file_size 是　int类型
    while has_send != file_size:
        # 表示把文件信息以1024字节一段一段的发,不是全发过去，所以就需要循环发，也需要个条件来判断什么时候发完
        # 注意：接收方也要重复接收
        data = f.read(1024)
        sk.sendall(data)
        has_send += len(data)
    f.close()
    print('上传成功')


sk.close()




