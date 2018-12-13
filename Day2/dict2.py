#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: dict2.py
@time: 2018/8/14 0014 下午 3:11
"""

# 定义一个字典

dict1 = {}
print(dict1)
# 看dict1的类型是什么
print(type(dict1))

# 字典只有一项 key value
dict1 = {'name': 'yang'}
print(dict1)
# 也可以把namekey赋值成'name'
namekey = 'name'
dict1 = {namekey, 'yang欧阳吉安'}
print(dict1)

dict1 = {'name': 'yang', 'age': 36}
print(dict1)

# 1表示一个key
dict1 = {'name': 'yang', 'age': 36, 1: [100, 200, 300]}
print(dict1)
# 但是不能这样放
# dict1={'name':'yang','age':36,[100,200,300]:Day12}
# TypeError: unhashable type: 'list'中unhashable ，hash表示哈西算法
# 表示[100,200,300]这个数组不能进行哈西算法，因为数组是动态的,list,dict,set都不是哈西类型数据（可变变量）
# 但是前面的 key 的键是字符串是钉死的

# 取字典的内容 字典对象[字典key]
myname = dict1['name']
print(myname)
mylist = dict1[1]
print(mylist)

# 设置里面的值 和 修改
dict1['name'] = 'Ann'
dict1['age'] = 100
print(dict1)

# 删除某一项
del dict1['name']
print(dict1)
# del 可以删除任何对象 也可以删除整个字典
# del dict1
# print(dict1)
# NameError: name 'dict1' is not defined 说明字典已经删除了 不能打印出来了

dict1 = {'name': 'yang', 'age': 36, 1: [100, 200, 300]}
# 如果想把字典清空 dict1 ---> {}
# 这种就是面向对象的清空方法，也可以用 dict1={} 但是这种是直接赋值，有本质区别
# dict.clear()是保持原来dict的对象不变，只是清空对象，但是赋值后就是一个全新对象
# 注意 del dict1 和 dict1.clear()有本质区别
# del是删除以后就不能使用  而clear知识把内容清空
dict1.clear()
print(dict1)
# 注意，clear是一个函数，但是不同于把函数放前面的形式:如print(xx)
# 是因为dict1,clear()是clear这个函数内置在了对象里面
# 这种面向对象的方法调用格式就是 dict1叫一个对象，那么调用对象的格式的方法就是：一个对象.对象里面的方法（对象.方法）
# Python里面 一切都是对象 比如： a 就是int对象

# 取得dict1里面的所有键key
dict1 = {'name': 'yang', 'age': 36, 1: [100, 200, 300]}
keys = dict1.keys()
values = dict1.values()
print(keys)
print(values)

# 判断name时候在dict里面
haskey = 'name' in dict1
print(haskey)









