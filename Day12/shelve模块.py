#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: shelve模块.py.py
@time: 2018/8/17 0017 上午 12:59
"""

"""
shelve模块,shelve返回类似字典的对象,只有1个 open函数,是基于pickle发展的可读可写
key键必须要是字符串，值是所有python数据库类型

"""

# FIXME 其实我一直没有明白  shelve 有什么用

import shelve

f = shelve.open(r'shelve_text')  # 文件名前一定要加 r , 表示原生字符串
# shelve 函数的 会以 .bak .dat .dir 3种格式来存取数据

f['info'] = {'name': 'alex', 'age': '18'}  # 表示 键 info 的值 是一个字典

# 获取信息用 .get
data = f.get('info')
print(data)  # {'name': 'alex', 'age': '18'}


#  get函数的使用
d = {'name': 'alex', 'age': '18'}
#  传统方法取键的值
print(d['name'])  # alex
# .get 面向对象的方法
print(d.get('name'))  # alex

# FIXME .get 后面跟2个参数 表示：如果对象第一个参数有值 就返回第一个参数值,如果没有就返回第二个参数值
print(d.get('name', 'male'))













