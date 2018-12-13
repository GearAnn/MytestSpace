#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: subprocess模块.py.py
@time: 2018/8/29 0029 下午 6:02
"""


# FIXME 必读!!!
"""
subprocess的目的就是启动一个新的进程并且与之通信。

subprocess模块中只定义了一个类: Popen。可以使用Popen来创建进程，并与进程进行复杂的交互。
"""


import subprocess

# 利用subprocess新开一个子进程,dir表示显示文件目录，stdout=subprocess.PIPE表示通过管道把子进程转到主进程
a = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE)

# 子进程执行完后就封装到了a里面,所以a就是一个封装后的对象
print(a)  # <subprocess.Popen object at 0x00000000023039B0>

# 既然a是一个对象，就可以进行调用
print(str(a.stdout.read(), 'gbk'))  # 结果为一个二进制的bytes类型,需要字符串进行转换
