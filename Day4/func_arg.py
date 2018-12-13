
# 自定义一个函数
# 函数尽管定义了 如果不调用 则不会执行 也就是跑不出来
# 函数定义依一次 就可以调用无数次

# 定义一个空函数


def test():
    # 这里就是函数定义的内容 定义为空且不带参数
    pass

# 定义带参数的函数


def test2(arg1):
    print('in test2', arg1)
# 参数类型没有关系 可以传入任意类型


test2(1)
test2("hello Python")

# 函数参数的调用


def test7(name, age):
    print(name, age)


test7('yang', 18)
# 关键字参数顺序可以交换，因为有关键字参数可以指定
test7(name='wang', age=18)
test7(age=20, name='An')
# 注意：Python里面如果参数位置顺序交换，必须先写普通参数 关键字参数放后面
# 错误的是 test7(20, name='An', 70) ,这里要把关键字放最后
# 还有如果同一个位置的参数，不能再用关键字赋另外一个值

# 默认参数
# test8有3个参数 但是可以


def test8(name, age, score=60):
    print(name, age, score)


# 但是只传入了2个参数 系统就自动认为缺位的参数为函数定义的值
test8("An", 18)
# 上述函数打印出来后 socre位置的参数自动认定为 60

# 但是如果函数定义是默认参数 但是还是可以传入参数
# 所以函数定义的默认参数 要放最后面，前面不能有普通参数 比如：
# def test8(name, age = 18, score):   (错误写法)
# 上诉这种就是错误的， 要把默认和关键字参数 都放后面
# def test8(name, score，age = 18,):  （正确写法）

"""
关键字参数的好处：
Day12.关键字参数可以交换顺序（没有必要）
2.有关键字参数可以让其他人读代码的时候更加清晰
"""

# 可变长参数的使用 语法：
"""
def printme(*args, **kwargs):
其中 *args表示普通参数  **kwargs表示关键字参数
"""
# 可变长参数的意义在于：自定义函数的时候也自动定义了无数个参数的个数
# 在调用函数的时候 不用一一对应参数的位置 比如：
# def test7(name, age):
#     test7('yang', 18)      (这里定义参数 和 参数赋值就是一一对应)
# 在可变长参数中 *args  args自动定义为一个元组类型


def test10(*args):
    print(args, type(args))
    value = 0
    for i in args:
        value += i
    return value


# 定义的函数表示为：打印出每一个参数 然后每个参数依次相加之和是返回值
c = test10(1, 2, 3, 4, 10, 100)
print(c)

# 可变长参数的变种：前面2个参数是默认固定位置v1,v2 后面是可变的


def test11(v1, v2, *args):
    print(1, 2)
# 这里v1,v2就必须用赋值去占位置


# 可变参数 传入 数组列表 语法
list1 = [1, 2, 3, 4]
# *list 就是把 数组列表 展开成 Day12,2,3,4
c = test11(1, 2, 1, 100, *list1)


# 可变参数处理关键字参数,注意 kwargs是字典 args是一个元组
# 其中一个*表示位置参数（普通可变参数,positional参数）
# ** 表示关键字可变参数
def test12(**kwargs):
    print(kwargs, type(kwargs))
# 因为是可变参数 所以空也是参数
# TypeError: test12() takes 0 positional arguments but Day12 was given
# 以上表示 test12()这个函数没有位置参数（就是普通参数）,但是调用的时候人工给出了普通参数
    value = 0
    for key in kwargs:
        v = kwargs[key]
        # 判断如果是int/float就相加
        if isinstance(v, int) or isinstance(v, float):
            value += v
    return value


test12(name='yang')
# TypeError: unsupported operand type(s) for +=: 'int' and 'str'
# 就是说 name也有可能不是int 也有可能是个字符串 所以要加个判断
c = test12(name=10, b=1, c=2, d=3, e=4)
print(c)


# 可变参数支持 位置参数和关键字参数(也叫二维可变参数)
def test13(*args, **kwargs):
    print(args)
    print(kwargs)
    value = 0
    # 先处理 位置参数
    for i in args:
        value += i
    # 再处理 关键字参数
    for i in kwargs:
        v = kwargs[i]
        value += v
    return value


c = test13(1, 2, 3, name=10, b=1, c=2, d=3, e=4, f=100.56)
print(c)


# 参数解开
dict2 = {'name': 10, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 100.56}
tuple2 = (1, 2, 3)
c = test13(1, 2, 3, name=10, b=1, c=2, d=3, e=4, f=100.56)
# *tuple2 表示把（Day12，2，3）解开成 Day12，2，3
# **dict2 表示把 'name':10,'b’:Day12 解开成 name=10, b=Day12 .....
# ** 这里的作用就是把dict2的字典 转换为 关键字参数
c = test13(*tuple2, **dict2)
print(c)
