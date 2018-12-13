#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: sever.py
@time: 2018/10/24 0024 下午 7:36
"""

"""
IO多路复用在socket中的应用

即：1个select可以监听多个socket对象,而且select在监听数据时属于水平触发，只要有数据存在那么select就会监听。

"""

import socket
import select


sk1 = socket.socket()
sk1.bind(('127.0.0.1', 6667))
sk1.listen(5)

sk2 = socket.socket()
sk2.bind(('127.0.0.1', 8080))
sk2.listen(5)
# sever绑定了2个端口8080和8081,2个socket对象sk1,sk2

while True:
    r, w, e = select.select([sk1, sk2], [], [])  # select([],[],[],数字)里面会有第四个参数，第四个参数代表监听的时间
    # 这里select就是在监听哪一个socket对象有数据传输
    # r就是一个列表， 装有有数据更新的socket对象，因为客户端是对接的6667端口，所以sk1才有数据更新
    # 所以 r列表 里面只有 sk1

    for i in r:  # r =[sk1]
        conn, addr = i.accept()  # r列表里面就只有sk1,所以 i 可以调用accept
        # FIXME 注意：IO模型的第一步（数据准备）recvfrom这个系统调用是accept或者select发送的
        print(conn)
        print('hello')
    print('>>>', r)
