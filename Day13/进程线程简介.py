#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: 进程线程简介.py.py
@time: 2018/8/11 0011 下午 9:50
"""
"""
一，现在操作系统os（windows,Mac,Linux,Unix）都支持多任务；
    单核CPU实现多任务的原理：各个任务交替执行，但是CPU速度太快导致看起来多任务是同时执行；
    多核CPU实现多任务的原理：如果任务多于核心，可能在某一个核心上也是交替任务执行；
    由操作系统来完成多任务的调度到CPU上。
    并发：看上去一起执行，实则任务书对于CPU核心（绝大多数都这样）
    并行：实则一起执行，任务数小于CPU核心（极少）

二，实现多任务的方式：
  1.多进城模式
  2.多线程模式
  3.协程模式
  4.多进程+多线程模式

对于操作系统而言，一个任务就是一个进程
进程是系统中任务执行和资源分配的基本单位。每个进程都有自己的数据段、代码段、堆栈段。
线程是调度操作系统的最小单位。
"""


# 单进程/单任务 现象
from time import sleep


def run():
    while True:
        print('sunck is a good man')
        sleep(1.2)  # sleep 是不占CPU的


if __name__ == "__main__":
    while True:
        print('sunck is a good man')
        sleep(1)
    # 不会执行到run,只有上面的while循环结束才可以执行
    # 但是多任务的话，多1个进程，就可以让2个while同时执行
    run()


"""
实现多任务，需要一个第三方库(multiprocessing库)，这是库是跨平台的多进程模块
提供了一个process类来代表一个进程对象
"""
# 通俗的理解__name__ == '__main__'：假如你叫小明.py，在朋友眼中，
# 你是小明(__name__ == '小明')；在你自己眼中，你是你自己(__name__ == '__main__')。
# if __name__ == '__main__'的意思是：
# 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行
# 当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
# 重点：
# 因为不管直接运行还是导入一个.py模块的时候，此.py模块还是会被执行一次
# 但是我们只想用.py的功能，不体现.py在其本身模块的具体值。所有就有了 if __name__ == '__main__'
# if __name__ == '__main__'就作为设定的Python程序的入口，使得此程序可以被导入，而不附加本身的值

"""
首先导入线程库(threading),线程的调用函数格式：threading.Thread(target= ,arg=())
"""
