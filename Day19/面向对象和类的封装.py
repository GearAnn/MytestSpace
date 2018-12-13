#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 面向对象和类的封装.py
@time: 2018/8/17 0017 下午 2:23
"""

# 定义一个函数
# 函数式： def + 函数（参数）

def foo(name, age):
    print('我叫 %s ,我年龄是 %s' % (name, age))


foo('小米', 19)
foo('夏明', 20)


# 定义一个类class 把函数式编程改为面向对象的编程
# 如果类里面有函数,那么这个函数就叫方法,且方法的第一个参数必须是 self

class Bar:   # Bar 是类的名字

    def foo(self, name, age):
        print('我叫 %s ,我年龄是 %s' % (name, age))


obj1 = Bar()  # 创建对象obj,且对象也可以赋值,通过对象/中间人去调用类的方法:foo
obj1.foo('Ann', 33)  # 我叫 Ann ,我年龄是 33

obj2 = Bar()  # 即不同的对象 可以引用同一个类

# 创建的对象也可以赋值 比如：

obj2.name = 'Alex'  # 表示　self.name 赋值 为　Ａlex


# FIXME 注意:创建对象的时候,自动创建了'类对象指针',表明这个对象和类的关联性,即对象可以调用类的函数
# FIXME 注意:切类的和对象的关联性不唯一,一个类可以关联多个对象,即多个对象可以调用同一类的函数


"""
类的三大特性之封装（用__init__实现）

引入新的概念：构造方法  
其作用：就是赋予class一个功能,让class可以自动执行一些内容

在 对象 = 类名（） 中, 即 在创建对象后,系统自动执行 __init__ 定义的函数

实现构造方法功能的格式必须是： 
   
   class 类名:      
        def __init__ (self)：              
             
            '这里添加需要类自动执行的内容'
        
        def 函数名（）： 
                    
构造方法的作用就是：
 一旦类赋予了对象, 则Python系统自动调用 __init__ 定义的函数,不需要手动去调用
这样就可以实现一些预先设定好的值的封装. 
"""


class Bar:
    def __init__(self):
        print('123')


z = Bar()  # 返回 123 此时系统就自动运行了一次 __init__定义的函数

print(z)  # 返回 z 为一个对象  <__main__.Bar object at 0x00000000023F59E8>


# 所以在有些情况下 在创建类的时候 有些东西是必须事先写好 所以放在 init 里面,创建好了自动执行
class Person:

    def __init__(self, name, age):
        self.n = name  # 这里人添加的内容，后面自动执行
        self.a = age

    def show(self):
        print('%s-%s' % (self.n, self.a))


Lihuan = Person('李欢', 22)  # 这就在给对象进行赋值，lihuan就是个对象，这样就把对象的值封装在了对象里面


Lihuan.show()  # 返回：李欢-22 show函数就把对象封装的值打印出来

































