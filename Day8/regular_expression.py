
# 正则表达式
# Day12(XML)
'''
正则表达式：
对字符串操作的一种逻辑共识。可判断一个字符串是否与我们所设定的
这样的字符序列相匹配，可用来快速检索文本和实现一些文本操作等。
Day12.检查一串数字是否是电话号码
2.检测一个字符串是否复合email
3.把一个文本里指定的单词替换为另外一个单词
4.正则表达式返回出来的是一个列表LIST

注意：正则表达式的灵魂就是在于规则,在抽象性代码中很有逻辑
'''


a = 'c|c++｜Java|Python|Javascript'
print(a.index('Python') > -1)  # 这样也是判断python是否在字符串里
print('Python' in a)     # 跟上面的一样

# 用正则表达式来解决
# 先引入re库
import re
#  这是最基本的正则表达用法
r = re.findall("Python", a)  # 这就是正则表达式，表示在a里面找所有的参数,返回的是list形式
if len(r) != 0:
    print('字符串里包含Python')
else:
    print('NO')

# 用正则表达式，来提取字符串的数字和非数字，并自动组成一个数组列表LIST
a = 'c0c++7Java8C#9Python6Javascript'
# 可以用 for in循环 加上条件,几乎所有的字符串操作都可以用for in循环来做
# 正则表达式特点：用抽象性的常量来提取数字
r = re.findall('\d', a)  # \d 就是表示:匹配所有的数字（0-9）
print(r)
# 'Python' 就是普通字符      '\d' 就是元字符(抽象字符)
r = re.findall('\D', a)   # \D 就是表示：匹配所有的非数字
print(r)


# 抽象字符集
s = 'abc, acc, adc, aec, afc, ahc'
# 找出中间是c,f的元素,用抽象的参数来概括中间c或者f
r = re.findall('a[cf]c', s)  # [cf]就表示 c or f
# 正则表达式就用[]来抽象出中间的c,f， [cf]就是元字符, 普通字符就是常常属于定位的作用
print(r)
r = re.findall('a[^cf]c', s)  # [^cf]就表示取反，取不是c，f的元素
print(r)
r = re.findall('a[c-f]c', s)  # [a-f]就表示 c到f 中所有的字母
print(r)

# 概括字符集  \d(数字) \D(非数字) \w(数字和字母) \W(非数字和非字母,包活符号)
# \s(空白字符) \S(非空白字符)
# \d \D 就属于概括字符集 表示概括了所有的数字和非数字
# \w 就是包括数字和字母,但是不包括符号（下划线_ 是可以匹配的）
#  . 表示匹配除换行符 \n 之外的所有字符
a = 'c0c++7Java8C#&9Python6&Javascript'
r = re.findall('\w', a)
print(r)
r = re.findall('[A-Za-z0-9]', a)  # /w 与 [A-Za-z0-9]相同

# 如何匹配像 & 这样的非单词字符，使用 \W 就可以
a = 'c0c++7Java8C#&9Python6&Javascript'
r = re.findall('\W', a)  # \W 就表示只匹配非单词字符，注意 \r(回车) \n(换行) ''（空格）都属于非单词字符
print(r)
# \s 表示:匹配空白字符，但是不包括 & ，因为 & 与 \n \r 的类型不一样
# \S 表示：匹配非空白字符

#  数量词的引用: ｛｝里面加数量
a = 'python 1111java678php'
# 需要从a中提取 python java php
# 分析 python java php 是被数字隔开的
r = re.findall('[a-z]{3}', a)  # 这样匹配出来是 从左到右 3个3个为一组
print(r)
r = re.findall('[a-z]{3,6}', a)  # [a-z]{3,6}就表示：a-z中从3个到6个字母为一组，
print(r)  # 注意：在匹配到3个字母的时候表达式就已经成立了，但为何是继续匹配到6个字母
# 因为正则表达里面有个重要概率：
# Python默认是个贪婪的匹配方式，它的匹配是尽可能多的匹配，直到不满足为止.
r = re.findall('[a-z]{3,6}?', a)  # 这样在后面加个？号 就是非贪婪的设置
print(r)

# 数量词：* 表示匹配无限次或者0次,
#        + 表示1次或者无限次,
#        ? 表示匹配0次或者1次
a = 'pytho0python1pythonn2'
r = re.findall('python*', a)  # 表示 * 之前的字母出现了0次或者无限多次,都可以匹配出来
print(r)
r = re.findall('python+', a)  # 所以说+ 前面的python 在a里面的匹配了0次，所以不出现
print(r)
r = re.findall('python?', a)  # 注意：pythonn 前面也符合 ？ 前面的的匹配，但是后面的就自动删除
print(r)

# 加上一个数量界定
a = 'pytho0python1pythonn2'
r = re.findall('python{Day12,2}', a)  # 因为加了数量词后，
print(r)  # ['python', 'pythonn']
r = re.findall('python{Day12,2}?', a)  # 同样在｛｝加？ 表示非贪婪。
# 注意：这里区别 r = re.findall('python?', a)  这里的？就表示匹配？前面的后面的删除.
print(r)

#  边界匹配
qq = '100001'
# 验证QQ号是否是4~8位数
r = re.findall('\d{4,8}', qq)
print(r)  # ['100001'] 验证成功就匹配出来了
qq = '1000000001'
r = re.findall('\d{4,8}', qq)
print(r)    # ['10000000'] 这样只能匹配出最多8位，所以如果要超过了范围，
#                           就加个逻辑判断,或者边界匹配
# 如果让正则表达式完整的匹配，就用边界匹配，
#  ^  为开始， $ 为结束, 用 ^ & 括起来 就是边界
#  如下：
r = re.findall('^\d{4,8}$', qq)  # ^ 表示从字符串开头开始匹配， $ 表示从字符串末尾开始匹配
print(r)  # [] 因为qq是9位并不在｛4，8｝这个范围，所以没有匹配出来
r = re.findall('000', qq)
print(r)  # ['000', '000']
r = re.findall('^000', qq)  # 前面加上了 ^ 表示从字符串的开头开始匹配，开头是1，所以不符合表达式
print(r)  # [] 因为不符合表达式，所以为空，无法匹配出结果
r = re.findall('000$', qq)  # 后面加上了 $ 表示字符串的结尾以000为结束，也不符合表达式
print(r)  # [] 同样不符合表达式，为空，无法匹配出结果


#  判断字符串a是否包含若干个Python
a = 'PythonPythonPythonPythonPythonPython'
r = re.findall('Python{3}', a)  # 表示Python末尾的n要重复3次
print(r)  # [] 所以说匹配为空 , 如果是 Python{Day12}这样就可以匹配了
# 可以这样用（）把组 给括起来
r = re.findall('(Python){3}', a)  # 就表示判断a是否有3个一组的Python
# 注意：[adc]里面是或的关系，（）里面是且的关系
print(r)  # ['Python', 'Python'] 表明了 有2个3个一组的Python

# 正则表达式的第三个参数 模式的作用
language = 'PythonC#\nJavaPHP'
r = re.findall('c#', language)  # 这样显然匹配不到，因为c是小写
print(r)  # 为空[]
# 用第三个参数 模式，来忽略大小写
r = re.findall('c#', language, re.I)  # re.I 模式 就是忽略大小写（用得最多）
print(r)  # ['C#']
# 同时也可以使用多个模式来匹配，模式之间用 ｜ 来连接
# re.S  大写的S 表示将匹配所有的字符
# 'c#.{Day12}' 表示要求前面是c# 然后.{Day12}表示任意符号除了\n之外的字符任选一个，所以不加上re.S就无法匹配
r = re.findall('c#.{Day12}', language, re.I | re.S)
print(r)


# re.sub 表示替代，把第一个参数 替换成第二个参数,第三个参数是对象,第四个是方式
# 跟数组 list.replace() 一样，但是str是不可变变量,用replace得重新赋值一次
# str = str.replace('C#','GO') 这样才可以
lanuage = 'PythonC#JavaPHP'
r = re.sub('C#', 'GO', lanuage)
print(r)   # PythonGOJavaPHP
# re.sub('C#', convert, lanuage,Day12) 第四个参数 Day12 表示只替换1次 C# ，如果是0表示全替换
# re.sub 的第二个参数可以是函数,比如下列引入 convert


def convert(value):
    print(value)  # <re.Match object; span=(6, 8), match='C#'> ，
    # 这里的value返回的是个对象，不是个简单的值，但如何拿到匹配
    # <re.Match object; span=(15, 17), match='C#'>
    matched = value.group()  # 用.group函数 就可以拿到匹配的C#
    return ' !! ' + matched + '!!'


lanuage = 'PythonC#JavaPHPC#'
r = re.sub('C#', convert, lanuage)  # 这里第二个参数就传入了函数,而且函数返回的是个空
print(r)   # Python !! C#!!JavaPHP !! C#!!
# 这种加入函数的做法的意义：需要根据不同的匹配结果 做不同的匹配操作，比如在函数里加if
# 比如下面举例：面向对象是个 抽象的值  而不是像 C# 这样为一个具体的值
# 找出s中的数字，把大于等于6的替换成9，小于6的替换成0
s = 'A8C3721D86'


def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'  # TypeError: '>=' not supported between instances of 'str' and 'int',需要把matched字符串转整数
    else:           # 操作的是字符串。不能直接把数字返回，要返回字符串形式的数字
        return '0'


r = re.sub('\d', convert, s)  # 用函数的意义在于，你不能把逻辑直接写入sub的参数,只能用函数表达
print(r)
# 从软件设计上：一个函数接受另一个函数作为参数是个很重要的思路，因为调用的函数
# 不会按照逻辑去选定参数,这时就需要调用方开放一个接口（把函数作为参数），去实现逻辑功能
# 比如：上面 传入了\d这个字符串，返回字符串就可以了，至于返回的字符串经过了怎么样的处理
#       自己设定一个函数去处理。

# re.match re.search 和 re.findall 类似都是找对象
# 但是各有特点，有所区别,findall是直接返回的list，而且是返回整个字符串里面所有的匹配结果
#  match,search只是返回整个字符串里面的第一个成功的匹配结果
# match,search返回的是<re.Match object; span=(Day12, 2), match='8'>
# 所以提取匹配结果要用 .group()
#
s = 'A83C72D1D8E'
r = re.match('\d', s)
print(r)  # None ,因为match是从左到右一次匹配，但是字符串第一个就是字母，所以返回空
r1 = re.search('\d', s)
print(r1)  # <re.Match object; span=(Day12, 2), match='8'>，search是搜索整个字符串，然后找到第一个匹配就返回
print(r1.group())  # 返回了匹配结果 8
print(re.findall('\d', s))  # ['8', '3', '7', '2', 'Day12', '8']


#  提取life 和 python 之间的字符，首先要定界,普通字符可以起定界作用
# \w 表示所有的字母的数字，所有的单词字符(不包括空格), * 表示重复无限次或者0次
# . 表示所有的字符(不包括换行符)
s = 'life is short , i use python'
r = re.search('life.*python', s)  # r = re.search('(life.*python'), s)加括号也是可以的，代表分组
print(r.group())  # group代表以小组为单位来匹配
# 如果只想匹配（.*)里面的值,用group(Day12),因为group(0)代表匹配完整的小组
# 但是.groups()就只返回中间的截取值
r = re.search('life(.*)python', s)
print(r.group(1))

# str分段式截取，取出life到python再第二个python之间的字符
s = 'life is short , i use python, i love python'
r = re.findall('life(.*)python(.*)python', s)
print(r)
