
# 使用while循环，即让电脑重复进行一系列动作
count = 1
print(0)
if True:
    print(count)
    count = count + 1
print(count)
# 现在我的需求是 我要从1开始打印 1000个，可以不断的继续写1000个print(count)
# 但是现在我们要用动态的去重复循环
# 就引出来来了 while

# while 的语法
"""
count=Day12
print(0)
while True:              （注意 while后面跟True是永远执行下去）
    print(count)
    count=count+Day12
print(count)
#这行的逻辑是这样的 从if开始执行到while
#然后while True，这个就是判断条件 是否满足 True
#满足就执行打印 和 加法 ,因为是while 所以执行完加法就马上重复从while的开头执行
#20行的print（count）是执行不到的，所以while就会陷入一个死循环， 下一个层次拥有执行不到
"""

# 现在 用while 执行到某个值 就停止循环
# 就在while 后面加条件 这样就是打印小于5

print('while begin')
count = 1
while count < 5:
    print(count)
    count = count + 1
'''
count=Day12   Day12<5  True
count=2   2<5  True
...
count=5   5<5  False  (有False就结束了)
 '''
print('while end')
# 所以 while退出循环的点的语法就是 while XXXX :
# 但是这种方法有缺点，那是因为退出的时候要返回到while后面的条件
# 条件判断是False才能停止循环，既是while层次的第一行来判断
# 但是不能在层次的最后一句来停止，若想层次最后一行停止循环 请看后面

# 计算从1加到100
print('"begin"')
a = 1
b = 0
while a <= 100:
    b = b + a
    a = a + 1
print(b)
print('"end"')

# 计算从1乘到10
print("'开始'")
a = 1
b = 1
while a <= 10:
    b = b * a
    a = a + 1
print(b)
print("'结束'")

# 用while层次的最后一句来停止循环的语法
# 最后一行用break 来停止循环
# 用True来执行一个永远的死循环，break可以停止整个while循环
# 即内嵌一个if 条件进入循环
print('"begin"')
a = 0
b = 0
while True:
    b = b + a
    print(a, b)
    if a == 100:
        break
    a = a + 1

print('"end"')

# 乘法
print('"begin"')
a = 1
b = 1
while True:
    b = a * b
    print(a, b)
    if a == 10:
        break
    a = a + 1
print('"end"')

# 一个死的无限循环 就是while True
while True:
    pass
# 一行循环 如果循环的语句只有一行可以简写
while True:
    pass
