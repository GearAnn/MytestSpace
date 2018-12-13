#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 程序传输Client端.py.py
@time: 2018/8/29 0029 下午 5:38
"""

"""
目的：

给对方传送一个程序命令，让对方执行，然后让对方把执行后的结果返回过来。

"""

# FIXME Client端


import socket

sk = socket.socket()

address = ('127.0.0.1', 8005)

sk.connect(address)

while True:

    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))

    data = sk.recv(1024)
    print(str(data, 'gbk'))  # 包含了汉字要用gkb

sk.close()

# client端: >>> 输入dir就是 在sever端上执行了，然后返回到client端上得出dir命令结果
#
# 驱动器 E 中的卷是 SSD
#  卷的序列号是 0001-AD45
#
#  E:\MytestSpace\Day21 的目录
#
# 2018/09/02 周日  下午 07:27    <DIR>          .
# 2018/09/02 周日  下午 07:27    <DIR>          ..
# 2018/09/02 周日  下午 06:43             2,408 (必读)subprocess模块
# 2018/09/02 周日  下午 07:14               963 subprocess模块.py
# 2018/08/29 周三  下午 05:37               188 __init__.py
# 2018/09/02 周日  下午 07:23               649 程序传输Client端.py
# 2018/09/02 周日  下午 07:27             1,226 程序传输Sever端.py
#                5 个文件          5,434 字节
#                2 个目录 71,214,411,776 可用字节


# fixme 注意：信息的连续发送可能会出现粘包现象，可以用time.sleep(),也可以重新conn.recv()一发一收重新阻塞
