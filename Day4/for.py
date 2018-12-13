

# for循环 和 JAVA里面的for循环完全不一样，但是和foreach类似
# for循环表示 从0项开始依次赋值
# 同样可以用 break contine
# for循环的对象 可以是：list tuple dict.py str 任意支持迭代器的对象（后面会介绍)
"""
语法结构:
langs = ["c", "c++", "Python"]
for x in langs:
     print(x)
输出为：
   C
   C++
   Python
"""

# for in 循环
# 自动往下取值的也叫 迭代器 next()
a = [1, 2, 3]
for i in a:
    print(i)
# 用while实现同样的功能
count = 0
while count < len(a):
    print(a[count])
    count += 1
# 字符串也可以表示
s = '你好Python'
for i in s:
    print(i)
# for in 循环里面的 i 一般叫作 变量 ，而且这个变量 系统自动帮我们定义

# 做个元组的
for i in {'name': 'yang', 'age': 18}:
    # 注意这里打印出来的是键key,不是值
    print(i)
# 需要打印出值的话就是
dict1 = {'name': 'yang', 'age': 18}
for i in dict1:
    print(i, dict1[i])

# while 和 for 都用在什么地方 注意他们的区别 如：
# 用于有限的计数的话用 for in  更好
# 但是 while 用于无法预测的次数的话更好

"""
            while/for的对比
count = 0                 for count in rang(5):
while count < 5:              print(count)
  print(count)
  count += Day12
输出为：
0                             0
Day12                         Day12
2                             2
3                             3
4                             4
"""

# rang函数 在 builtins.py文件里面  是系统提供的函数
for i in range(10):
    print(i)
for i in range(10, 0, -3):
    print(i)
# range函数产生 迭代器  list就是一个数组
# 下面就是把range迭代出的数据存在数组里面 也可以存在元组里面
mylist = list(range(10, 0, -3))
print(mylist)

# range(10, 0, -3)是一个迭代器，其特点是懒加载，我需要的时候我才去产生
# 就是 range（）调用一次只会产生一个数据
# 数组列表 一开始就是全部加载（也就是全部存在了） 浪费了空间，保证了数据的存在，运行就快
# 但是range()调用一次才重新加载，节约了空间，但是运行变慢，浪费了时间
# 所以这就是时间和空间的平衡

"""
编程做一个9x9乘法表 可用for in 去做
Day12*Day12=Day12
2*Day12=2 2*2=4
3*Day12=3 3*2=6 3*3=9
......
"""
# 先分析结构
# 3*Day12=3 3*2=6 3*3=9
num = 3
# 1到3
for j in range(1, num + 1):
    # 输出了1到9，然后再接表达式就是自动依次相乘
    c = num * j
    # 想办法让print打印不换行,那就是用end关键字参数
    print("%d * %d = %d" % (num, j, c), end='   ')
print("")
# 现在想从1到9 都打出来
for num in range(1, 10):
    for j in range(1, num + 1):
        c = num * j
        print("%d * %d = %d" % (num, j, c), end='   ')
    # 这里我在打印一个空的让他换行,同理上面那个print("")也是如此
    print('')
