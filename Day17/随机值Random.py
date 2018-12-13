#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 13:19
# @Author  : Ann
# @File    : 随机值Random.py
# @Software: PyCharm

import random

# random.random() 0到1的数 包括小数
print(random.random())

# random.randint(1, n) 随机1到n 包括n
print(random.randint(1, 8))  # 包括8

# random.choice('str') 随机在字符串里选一个字符
print(random.choice('hello'))

# random.choice(['str'，[],5]) 随机在list中选一组元素
print(random.choice(['str', [1], 5]))  # str,[1]

# random.shuffle() 洗牌，打乱顺序
a = ['str', [1], 5]
random.shuffle(a)
print(a)  # [5, 'str', [1]]

# random.sample([],n) 表示从list中随机抽取n多个值
print(random.sample(['str', [1], 5], 2))  # ['str', [1]]

# randow.randrange(1， n)  不包括 n
print(random.randrange(1, 5))  # 不包括5


# 制作一个5位验证码，由数字和字母随机生成
def v_code():
    code = ''
    for i in range(5):  # 表示循环5次, 后面跟循环的内容
        # random.choice随机在list中选一组元素 如下：
        add = random.choice([random.randrange(10), chr(random.randint(65, 91))])
        code += str(add)
    print(code)

v_code()


