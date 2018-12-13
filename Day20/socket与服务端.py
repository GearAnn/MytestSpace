#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: socket与服务端.py.py
@time: 2018/8/24 0024 下午 6:29
"""

"""
socket（套接字）是应用层（API)和传输层（TCP/IP）之间的一个抽象层。
socket中封装了一系列网络编程所需要的函数，包括建立TPC和UDP的函数，UNIX等。
并且socket中的参数是系统封装好了的,具体看函数解释。

socket封装的2种参数 TCP和IP地址：
  
  SOCK_STREAM(数据流): TCP （默认值）
  SOCK_Dgram: UDP

  
  family = AF_INET : 服务器之间的通信 IPV4 (默认值)
  family = AF_INET6 : 服务器之间的通信 IPV6
  family = AF_UNIX : UNIX不同进程间的通信    



socket通讯流程： 

TCP服务端                                                    TCP客服端

第一步： 创建socket    socket()                               第一步：创建socket             

第二步:  为socket绑定IP和端口号   bind()  

第三步： 监听设置端口，等待客户端的请求  listen()

第四步： accept阻塞，直到有客户端链接过来  accept()  <-----------  第二步：连接服务端


以上,服务端与客服端成功建立通信 利用recv() send() 发送和接收信息，此过程为客户端socket接口
"""

import socket

# family type
sk = socket.socket()  # 第一步：创建socket对象,()里面是默认值

print(sk)
# <socket.socket fd=220, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>

address = ('127.0.0.1', 8000)  # IP地址为本机地址,人为设定端口号为8000，注意：一般1024之前为操作系统的端口号

sk.bind(address)  # 第二步：bind绑定IP地址

sk.listen(3)  # 第三步：监听设置端口。 （3）表示等待通信请求的个数

print('waitting.....')

conn, addr = sk.accept()  # 第四步：阻塞，等待客户端链接。
# 阻塞：表示程序不再运行，只等待连接。一旦客户端链接成功，才会运行print(conn)
# FIXME 网络编程最重要的就是拿到conn，conn就是客户端的socket对象，conn是进行通信的通道
# FIXME 所以都是通过conn 来 send,recv
# FIXME 这里服务端向客户端发送信息

inp = input('>>>')
conn.send(bytes(inp, 'utf8'))  # 注意：python3里面传送内容是byte类型，用 bytes(对象,'utf8')

# 在Run界面 >>>后输入 hello 客户端就可以接受到 b'hello'
# 注意：发送汉字时 客户端的接收的是UTF8编码


# print(conn)  # 客户端连接后就会得到一个元组（包含2个变量） socket对象 和 客户端IP地址
# (<socket.socket fd=224, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0,laddr=('127.0.0.1', 8000),
#  raddr=('127.0.0.1', 50160)>, ('127.0.0.1', 50160))


# 最后关闭连接
# conn.close() 是关闭某一个客户端的socket通道
# sk.close()是关闭整个服务端所有的socket通道













