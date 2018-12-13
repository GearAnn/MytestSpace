
# 作用域
# scope 就是作用域的意思（视野）
# 表示value只能在本文件中使用,就是全局作用域 G
# 作用域的位置：模块（module），类（class），函数（def,lambda），lambda指闭包和嵌套
# if/elif/else/try/except/for/while不会产生局部作用域(其他的语言会产生)
value = 1000

a = 1
if a >= 1:
    print('if before change', value)
    value = 1001
    print('if before change', value)

print(value)
# 全局作用域 可以在if里面访问 同时也可以修改
# 全局作用域 好处就是可以在任何地方使用 ，缺点就是也可以在任何地方修改值的大小

for i in range(5):
    sum = 100
    # 在使用value
    value += i
print(value)
print(sum)
# 总结：在全局作用域里面 value也叫全局变量
# 哪怕是value/sum 写在for/while/if 里面，只要是在整个文件里面 都是全局变量
# 其他的语言是这个规定的：在if/while/for里面定义的变量，不是全局变量，是局部变量
# 但是一般来讲： 1、程序需要的是易读性，需要把变量和函数放在同一段落
#              2、for里面的 i 一般叫迭代器，一般也是全局的变量


# 局部作用域（一般是在函数定义里面产生）
def test(arg1):
    # arg1也是局部变量
    # 表示counter只能在test函数内部使用 不能在外面使用,这就是局部变量
    counter = 100
    print(counter)
    # sum3/counter都是局部变量，只能在def层次里面使用
    sum3 = 0
    for i in range(100):
        sum3 += i
    print(i)

# 在Python里面 def层次才会产生局部作用域，for/while/if都不会产生作用域
# 局部作用域的好处：在函数内部的变量 只能在函数内部自己使用
# 一旦出了这个函数 这些局部变量 会自动销毁
# Python的这种设计 就是便于新人学习，而不利于程序的阅读，因为你要往前面去找变量的值


# 函数内部可以访问全局变量
gsum = 123    # 这里gsum就是全局变量, 但是函数内部不能修改全局变量，如果要修改就必须内部作出申明 用global gsum
def test2():
    # 这里就是gloal就是申明 gsum
    global gsum
    print('gum is', gsum)
    # 因为前面申明了 所以可以对gsum进行修改
    # 否则函数内部就只能访问全局变量gsum，不能内部进行修改全局变量
    gsum += 1
test2()
# 每次调用的时候都会对参数进行 +Day12
test2()



