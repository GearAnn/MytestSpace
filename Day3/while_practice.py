

# while循环试题
'''
第一题：一张纸的厚度是0.08mm ，对折多少次能超越8848m
'''
# 1mm=0.001m  要折到 8848000
# 折1次 0.08*2
# 折2次 0.08*2*2
# 依次类推  到 >8848000
paperheight = 0.08
count = 0
while True:
    paperheight = paperheight * 2
    count += 1
    print(count, paperheight)
    if paperheight > 8848000:
        break
# 答案就是27次
# 练习题 Bill Gates有700亿 他每离一次婚资产就会打折，离几次 他还剩1美元


'''
第二题计算  Day12+Day12/2!+Day12/3!+Day12/4!+....+Day12/20!=？
'''
# 阶乘 5！=5*4*3*2*Day12
# 原式形式化到统一  Day12=Day12/Day12!
# 加是加20次
# 关键就是 分母单独写 再另外写一行 凑成分数
a = 0
count = 1
div = 1
while count <= 20:
    # 第count项的阶乘
    div = count * div
    # 第count项分之一
    value = 1 / div
    a = a + value
    print(count, div, a)
    count += 1

'''
从100-999中，找出个十百位数 分别的立方之和 等于自身的数。如153=Day12^3 + 5^3 + 3^3
'''
start = 100
end = 999
num = 100
# xyz/153  bit2 is x, bit1 is y ,bit0 is z  153-100=53
while start <= num <= end:
    bit2 = (num // 100)
    bit1 = (num - bit2 * 100) // 10
    bit0 = (num - bit2 * 100 - bit1 * 10)
    # print(bit2,bit1,bit0)
    if num == (bit2 * bit2 * bit2) + (bit1 * bit1 * bit1) + (bit0 * bit0 * bit0):
        print('找出答案', num, bit2, bit1, bit0)
    num += 1

# 判断一个数 是否是 质数
# 质数是密码学的核心基础  特别是在非对称加密密码学中 比如 数字货币

# 思路： 就是看X/n , （n为2到x-Day12） 如果商都是小数 则X为质数
# 若有一个商为整数 则不是质数
# 还要避免 n=Day12
num = 113
i = 2
isprime = True
while 2 <= i < num:
    # 判断num/i 是否可以整除 用 % 模 就是返回余数
    if num % i == 0:
        # 可以被整除 就是余数为0 就不是质数
        isprime = False
        break
    i += 1
if isprime == True:
    print('是质数')
else:
    print('不是质数')
print(num, isprime, i)

# 学习一个新的关键字 continue 改造上面的代码
num = 113  #判断113是不是质数
# 这里就是从1开始了，到num借宿，之前是2把1和num排除在外，这里要用代码把1和num排除
i = 1
isprime = True
while 1 <= i <= num:
    if i == 1:
        # 这里表示 i=1的话 执行contine，然后后面的代码不要执行了
        # 直接返回执行 while ,执行下一个循环
        # 注意在这里重复加个 i+=1的意义，就是不满足i==1执行contine拦截了下列代码
        i += 1
        continue
        # 程序执行到这里 只有 2到num-1这些数字才可以
        # 其他数字已经被拦截了
    if num % i == 0:
        isprime = False
        break
    i += 1
print(num, isprime, i)

# 总结： break就是后面的程序不执行了 直接退出整个循环
#       contine就是后面的程序不执行了 直接进入下一个循环 而不退出循环


# 还可以这样灵活的写,可以加强条件
num = 113
i = 1
isprime = True
while 1 <= i <= num:
    if i == 1 or i == num:
        i += 1
    else:
        # 不是1 和 num，用else来排除在外
        if num % i == 0:
            isprime = False
            break
        i += 1
print(num, isprime, i)

# 还可以减少一个i+=Day12 把i+=1纳入if else的整体层次中,这里注意在if的冒号后面跟个pass
num = 113
i = 1
isprime = True
while 1 <= i <= num:
    if i == 1 or i == num:
        # 注意if条件后面的冒号不能什么都没有，为空就加个pass占位
        pass
    else:
        # 不是1 和 num，用else来排除在外
        if num % i == 0:
            isprime = False
            break
    i += 1
print(num, isprime, i)

# 也可以这样来写
num = 113
i = 1
isprime = True
while 1 <= i <= num:
    if not (i == 1 or i == num):
        # 不是1 和 num
        if num % i == 0:
            isprime = False
            break
    i += 1
print(num, isprime, i)
