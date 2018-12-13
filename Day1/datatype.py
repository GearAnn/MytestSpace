
# 在这里我们开始操作编程

# 如何定义变量
# 定义一个变量a 然后把 10赋值给a
# Python是一门弱类型语言 系统会自动推导出正确类型
# C/C++ java，C# 强类型语言
# a表示整数类型

a = 10
b = 25
# print是系统的一个函数 表示打印到控制台
print(a)
print(b)
# 打印a和b 然后同时在a 和 b 之间加个空格
print(a, b)
# 把a-b的结果给c
c = a-b
print(c)
c = a*b
print(c)
# python3 / 是返回小数  python2也是返回整数
c = a/b
print(c)
c = b % a  # 取余数
print(c)
c = b // a  # 整除
print(c)
print(5**3)  # 5^3

# 浮点数小数的运算
a = 10.2
b = 25.3
c = a+b
print(c)
c = a-b
print(c)
c = a*b
print(c)
c = a/b
print(c)
c = b//a
print(c)

# 浮点数类型的函数 abs是一个函数
# 函数的规范是 名字（参数1,参数2）
# 没有参数 名字（） name() 1个参数 名字（参数1）
c = abs(-10)
print(c)
c = abs(-10.5)
print(c)
# 取得max()里面参数列表所有值中最大的一个
c = max(10, 20, 30, 40, -20)
print(c)
c = min(10, 20, 30, 40, -20)
print(c)
# c=5^3
c = pow(5, 3)  # # 5^3
print(c)
c = round(3.1415926)  # 四舍五入取整
print(c)
c = round(3.1415926, 2)  # 四舍五入取小数点后2位
print(c)

# 赋值里面有一个None
# 表示把d 赋值为没有 内容为空
d = None
print(d)

# 复数 实部 虚部
a = 10+21j
b = 20.5+10j
c = a+b
print(c)
# complex 面向对象的写法 括号前为实部 后卫虚部
a = complex(10, 20)
print(a)

# 做各种组合用法
c = 10+(20*100)+43/20
a = 10.3
b = 30.2
d = 10+(a*b)+(a/20)
print(d)

# 整数和小数float之间的转换
a = 100
# 把a整数转成小数float
b = float(a)
print(b)
# type(b) type是系统的一个函数 表示返回b的类型
# <class 'float'>
print(type(b))

a = 102.82
# 把a浮点数变化成整数
b = int(a)
print(b)
b = int(a+0.5)
print(b)
mytype = type(b)
print(mytype)




