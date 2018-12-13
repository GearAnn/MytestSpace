
# 字符串面向对象的使用

# 字符串的面向过程的使用
str1 = 'hello Python'

v = len(str1)
print(v)
v = type(str1)
print(v)
v = isinstance(str1, str)
print(v)

# 字符串面向对象的使用,这种面向对象的调用方法也叫点语法 dot.NET
v = str1.capitalize()  # 这个就是把字符串首字母大写,其他字母变小写，然后回返结果
print(v)
v = str1.endswith('Python')  # endwith()就是以（）为结尾,返回bool
print(v)

# find这个函数要注意：find()函数表示在str1里面是否有abc
# 有就返回abc在str1中的位置，没有就返回 -Day12
# 而且面向对象 自己会作为函数的参数，且为点号后面的第一个参数
v = str1.find('abc')
print(v)


# 2.list数组列表对象过程的方法
list1 = [1, 2, 3, 4, 5]
len = len(list1)  # 看长度
maxvalue = max(list1)  # 看list1中的最大值

# list数组列表面向对象的方法

list1.append(6)  # append表示往list1后面追加一个值
# def append(self, *args, **kwargs)：
# 表示append里面是2个参数，但是在调用的时候只有1个参数
# 这就是Python独有的特点：self不需要我们写，系统会自动把list1写给append
print(list1)

list1.clear()  # 就是把list1的数据清空,但是list1还在只是内容为空
print(list1)

list1 = [1, 2, 3, 4, 5]
list1.extend([100, 90])  # extend就是追加一个数组 合并成一个数组
print(list1)

c = list1.pop()  # pop()表示把list1最后一个元素给删除 再把删除的元素返回来
print(c)
print(list1.pop())
list1.pop(1)   # pop()中带参数表示删除指定位置的参数,并返回删除值
print(list1.pop(1))


list1 = [1, 2, 3, 4, 5]
# index（5）表示在list里面查找是否有5这个元素
# 如果有，就返回这个元素在list的位置（为第4项）,也叫list的index下标
# 如果没有，则 run 这个程序就会出错，但是在后续的异常处理会抓取这个异常
myret = list1.index(1)
print(myret)
# 也可以这样 避免index参数不在数组而导致的系统出错
# 使得index参数不在数组时 会返回


def myindex(listvar, obj):
    if obj in listvar:
        return listvar.index(obj)
    return -1


myret = myindex(list1, 6)
print(myret)
# 同时index（）还有一个功能
# def index(self, *args, **kwargs): 后面可以跟一个变量
# 可以指定index索引的位置从哪个位置开始到哪个位置结束 比如：
# list1.index(Day12,3)  表示 在list里面找1 但是从 3号位置开始找


list1 = [1, 2, 3, 4, 5, 3]
a = list1.count(1)  # count（Day12）表示计算参数1在list中出现的次数，也就是数数
list1.insert(3, 200)  # insert(3, 200)表示在3号位插入200
print(a)
print(list1)

list1.remove(3)  # remove(3)表示删除第一个出现的参数值，其他的同样参数值不删除
print(list1)
list1.reverse()  # reverse表示把顺序倒过来
print(list1)
list1.sort()  # sort 表示从小到大排序
print(list1)
list1.sort(reverse=True)  # sort(reverse=True)表示从大到小排序
print(list1)


#  3.字典的主要函数
dict1 = {'name': 'yang', 'age': 18}
dict1.clear()  # 把dict1内容清空
print(dict1)

dict1 = {'name': 'yang', 'age': 18}  # popitem（）就是从数组中删除最后一项元素
# 然后返回删除项，使之变成元组
myret = dict1.popitem()
print(myret)
print(dict1)

dict1 = {'name': 'yang', 'age': 18}
dict1.setdefault('cn', 'China')  # setdefault()如果字典里面没有cn这个键 ，setdefault就是设置默认值
# 那么就追加cn:China这个键值对，如果有同名的键 就不做任何处理
print(dict1)

#  update这个函数有3种用法，目的就是给字典里面增加 （key value pair）键值对
dict1 = {'name': 'yang', 'age': 18}
dict1['test'] = 'abc'  # 这是第一天学习的增加方法
# 第一种用法
dict1.update(score=99, glass=2)  # 这是用update增加的方法
print(dict1)
# 第二种用法
# def update(self, __m: Mapping[_KT, _VT], **kwargs: _VT) 表示
# 可以把一个字典追加到一个字典里面
dict2 = {1: '第一项', 2: '第二项'}
dict1.update(dict2)
print(dict1)

# 第三种用法
# def update(self, __m: Iterable[Tuple[_KT, _VT]], **kwargs: _VT) 表示
# 在字典里面追加了一个元组进去,但是元组要用[]来包裹,如上格式:[Tuple[_KT, _VT]]
dict1.update([('key2', 100), ('key3', 100)])
print(dict1)
# 在字典里面追加了一个数组进去，也要用[]来包裹,
dict1.update([['key4', 100], ['key5', 100]])
print(dict1)


# keys()表示返回字典里面所有的键key 然后把键kes组成在一起
# 返回的类型为：dict_keys（字典键）
myret = dict1.keys()
print(myret)
print(type(myret))
for i in dict1.keys():
    item = dict1[i]  # dict1[i]表示访问i项的值,但是这里的格式不用像之前学过的那样用dict['name'],这里省去了单引号
    print(i, item)
# 可以用for in循环 把所有的key,value都打印出来

# values（）表示返回字典里面所有的值value 然后把值value组在一起
# 返回类型为：dict_values（字典值）
myret = dict1.values()
print(myret)
print(type(myret))

# items()表示返回字典里面所有的 键值对（key和value）
# 返回类型为：dict_items
myret = dict1.items()
print(myret)
print(type(myret))
for key, value in dict1.items():  # 表示把键值对一起取出来，属于items函数的便利功能,不像上面.keys函数那样取值还要单独写代码
    print(key, value)
# 这样就能在程序开发里面通过dict1.items（）去通篇浏览字典


# 4.字符串str的面向对象的编程
s = 'hello Python'
# Python是一个解释性语言 Python console一般用来测试一些临时性的简单程序的运行、计算
# 介绍Python console 就是控制台 可以自动运行程序

# s.capitalize() 把首字母大写 其他字母小写
s.capitalize()

# s.center（x,y） 是把字符串放在中间,x表示居中的距离,y表示居中后空格用什么填充
# 空格不填充就是 s.center(x)
s.center(40, "*")
print(s.center(40, '*'))
# 结果就是
# **************hello Python**************

# s.count('X') 表示字符串s里面有多少个X，也就是数数
s.count('hello')  # 返回结果就是1，因为只有s里面只有1个hello
# 也可以从某一项开始数数，到某一项结尾,格式就是：s.count('x',5,10)
# 就是表示从第5项开始数数，到第10项结束

# s.encode（）表示显示s的编码，用来产生二进制编码或者十六进制编码
s.encode().hex()  # 表示显示字符串s的十六进制编码
print(s.encode().hex())  # 结果就是:68656c6c6f20507974686f6e

# s.endswith('x') 判断字符串s是否以x结尾，返回bool
s.endswith('Python')
print(s.endswith('Python'))  # 返回 True
# def endswith(self, suffix: Union[str, Tuple[str, ...]]）
# 上述 Union 就是表示 二个参数(str or tuple)二选一  比如：
s = 'hello Python'
s.endswith('Python', 3)  # 表示判断s的结尾 是否是Python or 3（二选一）
print(s.endswith('Python', 3))
s.startswith('python')  # 同理，判断以什么为开头


# s.find('x') 表示第一个x出现的位置，如果没有找到就返回 -Day12
s.find('hello')
print(s.find('hello'))  # 返回的就是第一个hello 在s的0号位置出现
# s.find('x',a,b) 同样也表示从第a项开始找到第b项结束

# s.format()表示把参数进行格式化输出
# s.format（） 表示:把字符串s里面需要替换的位置用｛｝编注位置,然后用（）里的参数替换然后格输出:
y = '这里有{2},{1},{2}'.format('Ann', 18, 17)
print(y)
# 也可以用关键字来标注位置,(注意:如果没关键字就用位置来标注)
y = '我叫{name},今年{age},得了{score}分'.format(name='Ann', age=18, score=17)
print(y)
# 跟字符串相加类似
a = '我是'
b = '人'
print(a + b)  # 表示：我是人

# s.index('x') 和 find类似, 就是找出x在字符串s的位置标号 否则就抛出异常
print(s.index('Python'))

s.isalpha()  # 表示:判断s是不是alpha数值 ，返回bool
s.isdecimal()  # 表示:判断s是不是decimal数值 ，返回bool   decimal表示十进制
s.isdigit()  # 表示:判断s是不是digit数值（阿拉伯数字），返回bool （这个用得最多）
s.isnumeric()  # 表示:判断s是不是numeric数值(包括中文,罗马) ，返回bool

# ''.join() 表示把()的参数连接在一起,参数放用['']包起来的字符串
# 也可以在''里面加符号,表示把每个参数用符号隔开
':'.join(['c', 'b', 'a'])   # 返回：'c:b:a'

'   ann  '.strip()  # 表示把字符串ann左右两边的空格去掉
'   ann'.lstrip()   # 表示把字符串ann左边的空格去掉
'ann   '.rstrip()   # 表示把字符串ann右边的空格去掉

# y.partition(':') 表示用冒号: 把字符串里面第一个值和其他值分割,且字符串必须用冒号：隔开
# 且分割完了后 是一个元组
y = 'a : b : c : d'
c = y.partition(':')
print(c)

# str.replace（'old','new'） 表示 把str里面old值 替换成 new值
# 后面的参数替换前面的参数,而且会替换多个同名的old值
'hello python'.replace('python', 'c++')

# str.split（'：'）就是把字符串str中用：分割的，重新分割成独立的小组
y = 'a :b ,c , d'
c = y.split(':')
print(c)  # ['a ', 'b ,c , d']


# s.swapcase()就是交换str的大小写
y.swapcase()
print(y.swapcase())
