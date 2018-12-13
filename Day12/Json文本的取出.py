#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: Json文本的取出.py.py
@time: 2018/8/16 0016 下午 11:25
"""


# 从JSON文本中取出信息/取出对象
import json

f = open('JSON_text', 'r')

data = f.read()   # 读取/获取文件信息
data = json.loads(data)  # 把json格式的文件转换为python格式

print(data['name'])  # 就可以取出 关键字值了


# JSON无法把函数,类转化为JSON字符串





