#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: Json1.py
@time: 2018/8/11 0011 上午 10:37
"""
import json
# Json的key，value需要加双引号
# json.loads()是	将json数据类型转换成Python数据类型（dict.py）
# json.dumps()是将 Python数据类型转化成json数据类型
# json的对象（object）在Python中表现为dict,在其他语言中就用其他的数据格式来搭载JSON
# 但是JSON无法把函数,类转化为JSON字符串

# FIXME json本质上是数据交换类型，可以看做是一种，标准化的中间数据类型
"""
json对象，json字符串，json的区别：
1.javascript是实现标准之一，标准就是(ECMASCRIPT-标准化的脚本程序设计语言),同样json也是实现标准之一
  可以看作是一种标准化语言,javascript是编写前端的主流语言，json和javascript没有特定联系。

2.跳出了语言的范畴就没有json对象这个说法，但是所有的概念都是基于javascript来说的

3.json有自己的数据类型，虽然json和javascript数据类型一模一样，但是两者不相等


专业的术语来描述：从某个对象的数据类型（一般为字符串）转换成某一语言的数据类型的解析过程
叫：反序列化
同理，
序列化：就是某一语言的数据类型转化成Json数据类型,但是python函数和类无法序列化为Json类型

"""
json_str = '{"name":"qique", "age":18}'  # Json字符串的标准格式
student = json.loads(json_str)
print(type(student))
print(student)
print(student['name'])
print(student['age'])

# 如果Json的object是数组列表结构（Json的数据类型一般4种：str,list/array,bool,number）
json_str = '[{"name":"qique", "age":18}, {"name":"qique", "age":18}]'
student = json.loads(json_str)
print(type(student))
# <class 'list'>,list中的每一个元素就成了字典dict
# 因为Python只能用dict来搭载json
print(student)



# 把 dic 写入 JSON_text 文档
dic = {'name': 'alex', 'age': 20}

data = json.dumps(dic)  # 转化为json字符串
f = open('JSON_text', 'w')  # w 模式自动创建文档

f.write(data)
f.close()
# 接着 json文本都取出  继续看



"""
如何把编程语言的对象存储在数据库？（因为数据库是二维表结构，不能直接存储对象）
方法1：可以把对象序列化成json/XML字符串，再把字符串存入数据库，使用的时候就提取再反序列化
方法2：可以把对象拆成二维表结构（推荐）
方法3：使用 NOSQL MongoDB 可以存储序列化后的对象(不推荐)

"""
# 为了保证代码的美观，把长数组分开写
student = [
             {"name": "qique", "age": 18}, {"name": "qique", "age": 18},
             {"name": "qique", "age": 18}
           ]




