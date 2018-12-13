#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Ann

# def sum(x):
#     a = 0
#     for i in range(1, 101):
#         a = i + a
#     print(a)


# 时间戳，从1970年Unix诞生开始到现在有多少秒
import time
time.time()
print(time.time())  # 1534387108.2460136秒

# 闹钟
time.sleep(0.1)  # 表示CPU在这停了0.1秒
print(time.clock())  # 计算CPU执行的时间

# .gmtime
print(time.gmtime())  # 元组类型的结构化时间，也叫时区时间，北京的东八区时间
# time.struct_time(tm_year=2018, tm_mon=8, tm_mday=16,
# tm_hour=2, tm_min=45, tm_sec=5, tm_wday=3, tm_yday=228, tm_isdst=0)

# time.localtime() 本地时间
print(time.localtime())  # 这就是北京时间

# time.strftime('%Y %m %d %H %M %S') 时间的字符串格式化输出
print(time.strftime('%Y %m %d %H %M %S'))  # 2018 08 16 13 02 06

# 单纯的表达当前时间
print(time.ctime())  # Thu Aug 16 13:09:34 2018

# time.mktime(对象) 表示：结构化时间/本地时间 转化为时间戳
print(time.mktime(time.localtime()))

# datetime
import datetime
print(datetime.datetime.now())  # 2018-08-16 13:17:50.531945






