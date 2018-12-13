#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: socketsever模块.py
@time: 2018/9/3 0003 上午 11:37
"""

"""
内容：利用socketsever模块搭建socket连接的框架，并实现并发聊天

注意：与Day21中建立聊天的区别在于Day21中的通信是1对1，其他的client端口在排队，没有实现同时通信


核心：
1.之前学习的socket的创建，IP/端口的绑定，监听，accept都封装到了socketservet模块里面
2.通过socketserver.ThreadingTCPServer(('127.0.0.1', 8091), MySever))这一句话就完成了socket的整个建立
3.通信的创建逻辑全在socketsever，所以只需要人为设置IP和端口
4.人为设定的类MySever(继承socketserver.BaseRequestHandler),把通信逻辑放在handle（）中

"""

# 调用 socketsever模块
import socketserver

# 自己定一个类，并继承socketserver.BaseRequestHandler库


class MySever(socketserver.BaseRequestHandler):

    # FIXME 重写一个handle()方法来实现和Client端的通信,所以所有的通信逻辑都放在了handle()里
    # FIXME 注意：利用socketsever模块建立的通信逻辑和自己创建的socket通信逻辑的区别
    def handle(self):
        print('服务端启动...')
        while True:
            conn = self.request  # 利用self.request来获取模块自创的conn,这里没有sk，所以等价于 sk.accept()
            print(self.client_address)
            while True:
                client_data = conn.recv(1024)
                print(str(client_data, 'utf8'))

                inp = input('>>>')
                conn.send(bytes(inp, 'utf8'))  # 通信逻辑就是服务端先接后发。

            conn.close()


# 利用socketsever模块建立socket连接的固定格式：
# 1.通过 socketserver.ThreadingTCPServer(('127.0.0.1', 8099), MySever))来建立连接，实现通信并发
# 2.通过 server.serve_forever() 来启动程序，包括执行类（上面的通信逻辑）

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8099), MySever)
    server.serve_forever()

"""
总结：
socketsever中包含了五个类:
1.BaseSever(最初的父类) 2.TCPSever 3.UDPSever 4.UnixStreamServer 5.UnixDatagramServer 
        +------------+
        | BaseServer |
        +------------+
              |
              v
        +-----------+        +------------------+
        | TCPServer |------->| UnixStreamServer |
        +-----------+        +------------------+
              |
              v
        +-----------+        +--------------------+
        | UDPServer |------->| UnixDatagramServer |
        +-----------+        +--------------------+

注意：除BaseSever以为，其他4个类都可以直接使用

"""

