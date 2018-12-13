#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 多进程类式调用.py.py
@time: 2018/10/10 0010 下午 6:31
"""

from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()
        # self.name = name

    def run(self):
        time.sleep(1)
        print('hello', self.name, time.ctime())

if __name__ == '__main':
    p_list = []
    for i in range(3):
        p = MyProcess()
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()