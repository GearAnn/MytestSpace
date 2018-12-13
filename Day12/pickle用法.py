#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: pickle用法.py.py
@time: 2018/8/16 0016 下午 11:18
"""

# FIXME pickle 的用法格式和 json 是一样的,pickle 弥补了 json 无法序列化Python函数/类的问题
# pickle python独有的数据类型,只能在PYTHON进行数据转换
"""
pickle 也是用 pickle.dumps() pikle.loads()
"""

import pickle
import json


def foo():
    print('ok')

# data = json.dumps(foo)  json.dumps 不能让函数foo 序列化
# TypeError: Object of type function is not JSON serializable

# 使用pickle 来解决,用法和json 一样 只是把模块名换成 pickle
# 用pickle 把函数foo 写入 JSON_text 文档


def foo1():
    print('ok')


data = pickle.dumps(foo1)  # pickle 序列化了函数 foo1

f = open('pickle_text', 'wb')
f.write(data)  # 但是写入后 查看文档 是乱码,这就是 pickle 的缺点
f.close()

# 虽然是乱码 但是可以取出来 用 .loads（）转换

f = open('pickle_text', 'rb')  # 第一步 打开文件

data = f.read()   # 第二步 读取文件/获取文件信息(乱码),注意：取出来的是函数foo1

data = pickle.loads(data)  # 取出foo1()函数，名为data
data()  # ok ,成功的取出了函数foo1，其执行结果为 ok









