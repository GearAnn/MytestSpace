
# return 返回值


def test4(arg1, arg2, arg3):
    print('in test3', arg1, arg2, arg3)
    # 返回1
    return [arg1, arg2, arg3] * 2


# 调用test2(Day12)函数 然后把返回值给ret变量
ret = test4(1, 2, 3)
print(ret)

# 如果函数没有定义返回值return  那么就是返回None


def test4(arg1, arg2, arg3):
    print('in test3', arg1, arg2, arg3)


ret = test4(1, 2, 3)
print(ret)


# 我们定义的函数 如果都是整数 那么返回数组
# 如果参数是字符串 就返回 字符串
def test6(arg1, arg2, arg3):
    print('in test6', arg1, arg2, arg3)
    # 要判断arg1 arg1 arg3是不是整数
    # isinstence(x,y)是系统函数 用来判断参数的类型
    # x表示参数，y表示参数的类型
    if isinstance(arg1, int) and isinstance(arg2, int) and isinstance(arg3, int):
        return [arg1, arg2, arg3]
    # 一旦return后 函数后续的代码就不会执行了
    if isinstance(arg1, str) and isinstance(arg2, str) and isinstance(arg3, str):
        return arg1 + arg2 + arg3


c = test6(1, 2, 3)
print(c)
c = test6('welcome', 'to', 'Python')
print(c)
