
#测试各种运算符

# 使用比较运算符
a = 10
b = 20
#（a == b）表示判断a 是否等于b 然后把判断结果返回给c
# 所以c只能是Ture 或者 False
c = (a == b)
print('c is', c)
# c是bool类型  boolean布尔
print('c type is', type(c))

# 判断a 不等于b 如果a的确不等于b 那么c=True
c = (a != b)
print(c)
c = (a > b)
print(c)
c = (a < b)
print(c)

c = (a >= b)
print(c)
c = (a <= b)
print(c)

# 赋值运算符
# 把10 赋值到a这个变量里面
a = 10
# a+=100 就是a=a+100
a += 100
print('a is', a)
a -= 200
print('a is' , a)
b = 11
a *= 11
print("a is", a)
a /= b
print("a is", a)
# 常量和变量 a b这种叫变量 常量是100 200常数
a **= 2
print("a is", a)
a //= 2
print('a is', a)

# 逻辑运算符
a = 10
b = 20
# and前后表达式 需要2个同时成立为True
# 那么返回值才是True
c = (a < b) and (b < 100)
print(c)

c = (a < b) and (b < 10)
print(c)

# or操作 or前后表达式只要有一个是True就是True
# 否则是False
c = (a < b) or (b < 10)
print(c)

c = (a > b) or (b < 10)
print(c)

# not
c = not (a > b)
print(c)
# 逻辑运算符 and 需要前后都是True 结果才是True 否则False
#           or  前后都是False 结果才是False 否则是True
#           not 取否定
# 表达式就是一个语句 一段程序运算

# 成员运算符 in/not in 在字符串和数组里面详细讲解
# 身份运算符 is/is not 主要是用在对象的对比 而不是比较内容
