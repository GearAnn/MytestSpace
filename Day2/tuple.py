
# 创建一个tuple元组
# 空的元组
item = ()
print(item)
print(type(item))

item = ('yang', 37, 99.9)
print(item)
# 也可以这样写
item = 'yang', 37, 99.9
print(item)

name, age, score = 'yang', '37', '99.9'
print(name)
print(age)
print(score)

# 取值
item = ('yang', 37, 99.9)
print(item[0], item[1], item[2])
print(item[1:2])
# 元组里面有 名字 年龄 数组 3项
list2 = [100, 200, 300]
item = ('yang', 37, list2)
print(item[2])
# 把元组里面的第二项取出来 赋值给list3
list3 = item[2]
# 再把list3的第二项赋值0
list3[2] = 0
print(list3)
# 不能修改指的是元组里面的内容不能修改，但是不包括元组里面的某项指向的内容
# 因为元组里面的第二项是数组list2，数组list2就可以修改,如下
item[2][2] = 0
print(item)
# Python对象里面的值和引用 string(字符串) int float tuple都是值
# 引用是 list dict.py ，引用是可以修改的

# 元组和数组的转换
item = ('yang', 37, list2)
list4 = list(item)
print(list4)
# 数组转换成元组
list5 = ['yang', 37, [100, 200, 0]]
tuple2 = tuple(list5)
print(tuple2)

# 在什么时候用元组和数组，就是看是否希望对方修改自己的值
# 若不希望对方修改，则转换为元组，在传给对方

# 求长度 len in
lentuple2 = len(tuple2)
hasyang = 'yang' in tuple2
print(lentuple2)
print(hasyang)
