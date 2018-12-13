#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: 协程实现爬虫功能.py
@time: 2018/10/18 0018 上午 9:29
"""

from urllib.request import urlopen
import gevent
from gevent import monkey
import time
# 猴子补丁用来最大成都监听IO阻塞，可以让windows下的IO阻塞切换效果更好
monkey.patch_all()


def f(url):
    print('Get:%s' % url)
    resp = urlopen(url)
    data = resp.read()
    # with open('xiaohua.html', 'wb') as f:
    #     f.write(data)
    print('%d bytes received from %s.' % (len(data), url))

# f('http://www.xiaohuar.com/')


start = time.time()
# 标准格式:gevent.joinall([gevent.spawm(f,'url')])
gevent.joinall([gevent.spawn(f, 'https://www.python.org/'),
                gevent.spawn(f, 'https://www.yahoo.com/'),
                gevent.spawn(f, 'https://github.com/'),
                ])
print(time.time() - start)

# FIXME 这里爬网站也可以用for循环去一个一个的爬取，但是速度慢，没有协程快
