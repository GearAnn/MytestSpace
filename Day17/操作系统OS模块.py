#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 14:25
# @Author  : Ann
# @File    : 操作系统OS模块.py
# @Software: PyCharm

# 调用操作系统的模块：提供对OS进行调用的接口
# 在这里执行和在cmd里执行是一样的
import os
# os.getcwd()
print(os.getcwd())  # 获取当前工作目录
# E:\MytestSpace\venv\Scripts\python.exe E:/MytestSpace/Day17/操作系统OS模块.py
# E:\MytestSpace\Day17

# os.curdir 'current dir' 表示返回当前目录
print(os.curdir)  # 返回一个 "." 表示返回当前目录

# os.pardir 'parents dir' 表示返回当前目录的父目录
print(os.pardir)  # 返回一个 ".." 表示返回当前目录的父目录

# os.chdir() ‘chdir：change dir’
# 改变当前的工作目录,变为（）里面的路径,表示改变到c:\Users中
# os.chdir(r'c:\Users')  # 注意格式chdir(r'盘名：\文件名')

# 创建文件夹
# os.makedirs('')  这个可以创建多层嵌套文件夹,比如('文件夹1\\文件夹2\\文件夹3')

# os.mkdir('dirname') 这个就不能创建对层嵌套，只能单层，但是可以重复使用,实现嵌套文件夹
# os.mkdir('dirname\\dirname1') 多次使用实现嵌套多层文件夹

# 删除文件夹
# os.rmdirs('')  这个只删除当前文件夹
# os.removedirs('')  这个只能删除空文件夹,如果上层为空，自行删除上层空文件夹

# 删除文件,不能删文件夹
# os.remove('') 这个是删除文件,不是文件夹


# 展示xxx文件夹,注意加 ‘r’ ,前面 os.chdir(r'') 也要加 r
os.listdir(r'e:\MytestSpace')
print(os.listdir(r'e:\MytestSpace'))

# 重命名文件
# os.rename('oldname', 'newname')


# FIXME 重要指令: os.stat('.\\文件名') 表示显示文件信息,修改时间，访问时间等
info = os.stat('.\\操作系统OS模块.py')
print(info)
print(info.st_size)  # st_size=1910 表示文件大小 1910字节
"""
os.stat_result(st_mode=33206, st_ino=13792273858822206,st_dev=109893,st_nlink=1,
st_uid=0, st_gid=0, st_size=1910, st_atime=1534427413, st_mtime=1534427413, st_ctime=1534415552)
"""

# 显示系统路径分割符
print(os.sep)  # 返回 '\' 表示 windows下用 '\' 来分割路径,如下：
# E:\MytestSpace\venv\Scripts\python.exe
# 跨平台的时候 就可以看路径的设定 比如 Linux 就用 '/' 来分割

# windows里面换行符是 \r\n ,linux是 \n


























