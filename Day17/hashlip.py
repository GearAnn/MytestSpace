#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: hashlip.py.py
@time: 2018/8/16 0016 下午 10:12
"""
'''
hashlib 可以生成算法用来代码加密 比如：

'abc'(明文) >>>>>>>通过一个算法转换为>>>>>>>'11238ssasa1fdasd181'（暗文）
但是是一种单向的加密方法
'''

import hashlib

# 第一种加密算法 hashlib.md5
m = hashlib.md5()  # 算法的名字就是 md5
print(m)  # <md5 HASH object @ 0x0000000001DA7DF0>

# m.update('hello world'), 通过 m hashlib算法 来加密 'hello world'
m.update('hello world'.encode('utf-8'))  # python3里面字符串都是 Unicode 类型,要编码成 utf-8
# 完成加密后 在用与 md5 配套的 .hexdigest（） 来获取密文
print(m.hexdigest())  # 5eb63bbbe01eeed093cb22bb8f5acdc3
'''
第一步：把 hashlib.md5（）算法 赋予 m
第二步：用m.update 对'hello world'进行了 m算法 加密
第三步：用与md5 配套的 .hedigest 来获取密文
 '''

# 第二种加密算法 hashilib.sha256()
# 同样三步,算法赋予对象, 加密字符串, .hexdigest()获取密文
s = hashlib.sha256()
s.update('hello world'.encode('utf8'))
print(s.hexdigest())  # 密文：b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9

















