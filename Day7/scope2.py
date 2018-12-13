

# 闭包（closure）作用域
gvar = 10000
def test():
    print('in test')
    # 局部变量
    testvar = 100

    def test2():
        value = 200
        # 注意 value只能在test2 里面使用
        # if no global gvar这里testvar的变量在 闭包test2()里面没有 就使用了闭包test2()外的testvar值
        # gvar not in local,outside of closure,so find it in global
        # __name__ belong built-in
        global gvar
        gvar += 1
        # above here changed global parameter
        print('in test2 change global', gvar, __name__)
        # change testvar,its not global,its local,so use nonlocal for change tesvar
        nonlocal testvar
        testvar += 1
        print('in test2 change closure variable', testvar, __name__)

    test2()
    print(testvar)
test()
# 一个函数要修改自己返回之外的变量，有两种情况
# 1、这个变量是全局的 用 global来申明
# 2、这个变量是局部变量，用 nonlocal 来申明

