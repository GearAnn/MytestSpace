
for i in range(1, 10):
    a = i**2
    b = i**3
    print(i, a, b)

a = ('{}爱他的{}'.format('小明', '钱'))
print(a)


dict1 = {'name': 'Ann', 'age': 18, 'score': 100}
print(dict1.items())
for key, value in dict1.items():
    print(key, '   ==》  ', value)

name = ['Ann', 'Liu', 'Li']
age = [18, 17, 19, 20]
for a, b in zip(name, age):  # zip表示 从左到友一次匹配
    print(a, '->', b)

wish = 99
word = [100, 20, 123, 134, 33, 99, 12, 99]
for i in word:
    if i == wish:
        print('找到wish了')
        break
else:
    print('No')


# 打开某以文件，然后进行循环读取，然后关闭 用with, wish可以自动关闭操作完后的文件
'''
with open('data.txt') as f:
    for line in f:
        print(line)
'''
# Python的数据类型：哈西hash类型（不可变变量），不可hash哈西类型（可变变量）
# 不可hash类型：list,dict.py,set,他们不可作为字典的键key

I = 10088
hex(I)  # 转为十六进制
oct(I)  # 转为八进制
bin(I)  # 转为二进制


# 从1加到100
a = 0
for i in range(101):
    a = a + i
print(a)


# 对2个序列进行处理
names = ['Leo', 'Ann', 'Yang']
ages = [23, 56, 25]

for names, ages in zip(names, ages):
    print(names, ages)





