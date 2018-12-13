
# 参数的传递：值传递 和 引用传递
# 这里可以看出来 agrs修改了 并没有修改a的值
# 这种就叫值传递参数，为什么呢？？后面会介绍原理


def test(args):
    print(args)
    args = 2
    print(args)


a = 1
test(a)  # 1 2
print(a)  # 1
# 值传递就是说 int,float,bool,complex,str,tuple
# 如果参数是以上这些类型 那么在函数内部不会修改传入的参数值
# 注意不包括数组列表list 字典dict 和其他自定义对象


# 引用传递
def test2(args):
    print(args)  # [1, 2, 3]
   
    args[0] = 100
    print(args)


list2 = [1, 2, 3]
test2(list2)  # [100, 2, 3]
print('调用完test2（list2）之后', list2)
# 上面可以看出来  如果参数是列表数组 那么函数内部可以修改传入的参数值
# 这种就叫做“引用传递”：可以对 list dict.py object（一切自定义对象）做参数传递


def test3(args):
    print(args)


dict3 = {'name': 'yang', 'age': 18, 'score': 100}
test3(dict3)
print('调用函数test3(dict3)之后的值是', dict3)
# dict也在函数test3中被修改了 修改后的值就会变化
