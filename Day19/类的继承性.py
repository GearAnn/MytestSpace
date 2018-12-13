#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 类的继承性.py
@time: 2018/8/17 0017 下午 5:45
"""

"""
子类和父类 例如：

class A():               
    def func1(self):
       pass
    def func2(self):
       pass
          
 
class B(A):              # 此时在类名（）里面的就是父类, （）外的是子类
    def func3(self):     # 即： A-父类（基类）  B-子类（派生类） 
       pass      


结论:
 
 B(子类)继承A(父类)的所有函数方法

"""

class F:

    def f1(self):
        print('F.f1')

    def f2(self):
        print('F.f1')

class S(F):

    def s1(self):
        print('S.s1')


obj = S()

obj.f1()  # F.f1  S类继承了父类F的函数


# 以上是子类全继承父类，如何不继承父类,只有子类自己单独重新写个函数

# 如果父类和子类里有同样的函数,系统会默认执行面向对象所在的类，但是如何要求
# 子类和中指定执行父类中的函数  用super 来解决

class F:

    def f1(self):
        print('F.f1')

    def f2(self):
        print('F.f1')

class S(F):

    def s1(self):
        print('S.s1')

    def f2(self):      # f2函数与父类中的同名
        super('S,self').f2()   # super代指父类,表示找到父类，执行父类的f2(),这是第一种写法
        print('s.f2')
        F.f2(self)  # 这是第二种调用父类的写法跟super等价
        # 这样就 执行了父类中的f2的方法

# FIXME  Python中 一个子类还可以继承多个父类
# FIXME  比如：class S(father1,father2): 但是在同名函数的情况下,先执行左边第一个父类
# FIXME  但是在同名函数的情况下,先执行左边第一个父类,且如果父类中还有父类，则一直一条线继承下去，
# FIXME  若多个父类有共同的根，则共同根的优先级是最后执行











