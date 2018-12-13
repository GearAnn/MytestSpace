#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 生成器.py
@time: 2018/8/13 0013 下午 9:56
"""

# FIXME：生成器和迭代器的区别，生存器的内容不在生成器里面（内容未生成，为空），而迭代器的内容在迭代器里面
# FIXME: 生成器在你需要数据的时候立即生成，迭代器在需要数据时是从迭代器这个容器中拿出来
# FIXME: 但生成器同时也是一个可迭代对象(Iterable),内部有_iter_方法的就是可迭代对象，比如 tuple list dict.py set
# FIXME: 所以生成器更节约内存，速度更快，但是只能一个一个去依次进行元素的操作，不像list可以任意调用元素
# 生成器：把列表生成式的[]换成（）
s = (x for x in range(1, 11))
print(s)  # <generator object <genexpr> at 0x00000000021435E8>

# 调用生成器中数据的方法：用 next(对象)或者 对象._next_
print(s.__next__())  # Python2 的写法
print(next(s))   # 等价于 print(s.__next__())

# 对于大数据而言，只能用循环来依次取值生成器的值
# FIXME Python的垃圾回收机制：当内存里的信息地址没有被变量引用的时候，就会被Python解释器回收
for i in s:
    print(i)  # 这样就调用了 生成器s 的内容



# 生成器有2中创建方式：
# 1.使用列表生成式的方法：（x*2 for x in range(1,2)）
# 2.使用yield
def foo():
    print('OK')  # 调用foo的时候，并没有执行,这就是不同与其他函数的地方，生成器只能通过next执行
    yield 1      # 生成了一个 1

    print('OK2')
    yield 2

g = foo()
print(g)  # <generator object foo at 0x0000000001E337C8>
next(g)  # 里就是生成器通过next执行了，得出 OK ，而且只生产 1个
next(g)  # OK2  到这里生成器就结束了，就只有2个内容

# FIXME  下面为什么不能写成 for i in g:
for i in foo():
    print(i)


# .send()方法
def bar():
    print('Ok1')
    count = yield 1
    print(count)

    yield 2

b = bar() # 创建生成器对象
a = b.send(None)  # 第一次的时候只能赋值None 这里等于 next(b),等一次send前如果没有next只能传None
# .send()等于next(),但是send()可以给yield赋值
print(a)
g = b.send('eee')  # 因为生成器第二个调用，从上次结束的yield 1开始，所以把'eee'赋值给了 count
print(g)  # 生成的 2



# 生成器也可以用yield实现一个伪并发，和协成差不多
import time

def consumer(name):
    print('%s 准备吃包子啦' %name)
    while True:            # 这里用while True表示一直生成，打破了生成器的次数限制
        baozi = yield
        print('包子 %s 来了，被 %s 吃了' % (baozi, name))

def producer():
    c1 = consumer('A')
    c2 = consumer('B')
    next(c1)
    next(c2)
    print('老板开始准备做包子了')
    for i in range(1, 11):
        time.sleep(1)  # 表示老板做包子的速度是1秒做1次
        print('做了2个包子')  # 1次做2个
        c1.send(i)  # 这里send和next一样不受 sleep的暂停,传入到内存
        c2.send(i)  #

producer()
# A 准备吃包子啦
# B 准备吃包子啦
# 老板开始准备做包子了
# 做了2个包子
# 包子 1 来了，被 A 吃了
# 包子 1 来了，被 B 吃了