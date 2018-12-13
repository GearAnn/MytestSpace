
# 闭包 closure (也叫函数的嵌套 nested)
"""
闭包的定义：
若一个内部函数对外部作用域（不是全局作用域）的一个变量进行引用，则称这个内部函数为闭包。
因为局部作用域的存在，在函数内部的变量，只能在函数内部自己使用
一旦出了这个函数 这些局部变量 会自动销毁，而闭包可以在外部进行调用，次为闭包现象
闭包 = 内部函数 + 定义函数时的环境

"""
# FIXME
def outer():
    x = 10   # x=10就是函数内部的变量，只能函数内部使用
    def inner():  # inner是内部函数
        print(x)  # x是外层的一个变量,

    return inner  # inner就是一个闭包 closure，成为了

f = outer() # 调用一次outer,使其函数指针指向inner
print(f())  # 因为f是一个闭包函数，闭包之外的局部变量x=10出了作用域并没有被摧毁，所以才可以在外部调用内部的inner
# 闭包 = 内部函数 + 定义函数时的环境


#
def test():
    print('in test')

    def test2():
        print('in test2')
    # 既然test2在test的内部 所以内部里面可以调用 但外部不能直接调用
    # 这样在比较复杂的函数的时候，就可以实现模块化工作
    test2()


test()
# test2()在外部不能执行，是因为test2()是nested在test()的函数
# 这样就可以实现我们的封装 面向对象的特点之一就是封装
# test2() 这种就是闭包 也叫 函数嵌套函数

# test4返回一个函数


def test4():
    print('in test4')

    def _add(a, b):
        return a + b
    # 返回一个函数的名字 专业术语 就是返回一个函数的地址 或者 指针
    # 就是说调用了test4()后 返回到_add（）这个函数上去
    return _add


# 证明: c 就是一个 func
# 因为c这里一调用test4() 就返回到了一个函数的地址 此时c就成为了 _add定义的函数
c = test4()
print(c, type(c))
# 可以看出 c 是一个函数
d = c(100, 200)
print(d)


# 改造上面的代码
def test5(arg):
    def _add(a, b): return a + b

    def _sub(a, b): return a - b

    def _mul(a, b): return a * b

    def _div(a, b): return a / b

    if arg == 'add':
        return _add
    if arg == 'sub':
        return _sub
    if arg == 'mul':
        return _mul
    if arg == 'div':
        return _div
    return _add


# 这里c调用的函数都是一样的（test5）,只是在同一个函数下每个的闭包是不一样的
c = test5('add')
print(c(100, 200))
c = test5('sub')
print(c(100, 200))
c = test5('mul')
print(c(100, 200))
c = test5('div')
print(c(100, 200))

# 函数作为参数值 传入 也叫 函数指针
# 主要用在回调callback 和 代理设计模式中

# 函数作为参数进行处理


def add(a, b): return a + b


def sub(a, b): return a - b


def mul(a, b): return a * b


def div(a, b): return a / b


def test6(a, b, func):
    v = func(a, b)
    return v


# 传入的第三个位置参数func 就是函数add
# 然后函数add替代了位置参数func 使得v = add(a,b)
# 所以这里 函数定义的func位置参数不用动，直接改变量就OK
c = test6(100, 200, add)
print(c)
c = test6(100, 200, sub)
print(c)
c = test6(100, 200, mul)
print(c)
c = test6(100, 200, div)
print(c)
# 这叫回调callback


# 加入新的语法
def add(a, b): return a + b


def sub(a, b): return a - b


def mul(a, b): return a * b


def div(a, b): return a / b


def test6(a, b, func):
    # 所以可以加入一个判断条件 用callable（func）来判断func是不是函数
    if not callable(func):
        return None
    v = func(a, b)
    return v


# TypeError: 'int' object is not callable
# c = test6(100, 200, 111) 表示了 111(100,200) 这里显然是错误的
# 因为111 在此不是一个函数无法调用 除非定义了111是个函数
# 所以可以加入一个判断条件 用callable
c = test6(100, 200, 111)
print(c)
