#!/usr/bin/python
# coding: utf-8

"""
@version: Python3
@author: Ann
@contact: 494792590@qq.com
@software: Pycharm
@file: 进程的数据共享.py
@time: 2018/10/10 0010 下午 10:05
"""

# FIXME 进程的数据共享通过 Manager 来实现


from multiprocessing import Process, Manager

"""
下列代码就是说明了，可以通过manager来实现多进程来同时修改数据

"""

def f(d, l, n):   # f 表示创建字典d赋值（创建键值对） , 对l列表进行添加值
    d[n] = "1"
    d["2"] = 2
    d[0.25] = None
    l.append(n)
    # print(l)


if __name__ == "__main__":
    with Manager() as manager:  # with open () as f==  f=open()  manager=Manager()
        d = manager.dict()  # d 就是一个字典 但是是由manager创建了，这样就可以在进程里实现数据共享

        l = manager.list(range(5))  # 同样通过 manager来创建list来实现数据共享
        p_list = []
        for i in range(10):  # 创建 10 个进程
            p = Process(target=f, args=(d, l, i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)

"""
难点：
以上代码是创建了10个进程，每个进程是在空字典里创建了3个键值对，原本是字典中会出现30个键值对，但是由于manager实现了数据共享，所以就不会单独的创建
多余的相同数据(相同的数据就会被覆盖掉)，而是在不同的数据上进行修改添加，所以由于d["2"] = 2 ，d[0.25] = None  是定值，而d[n] = "1" 中含有
参数，所以10个进程就只修改添加了不同的d[1],d[2]等，结果就是不变的2个键值对  加上 参数变动的10个键值对，一共字典中出现12个键值对 
 
"""