
# 字符串的操作测试模块  module

# 字符长度定义 以""包含的内容就是字符串
# 字符串也可以用单引号来定义
str0 = "hello"
print(str0)
# 若双引号里面也要输入双引号 需要加入反斜杠 \
# 反斜杠 \ 叫做转义字符
str1 = "hello\"你好\""  # hello"你好"
str2 = 'world'
# 单引号里面需要另外加入单引号同理加入 \
# 如果不用转义字符\ 可以在单引号里面加双引号
# 同理双引号里面可以加单引号
# 但是单引号里不能加入单引号，双引号里面不能加双引号
str3 = 'world"你好"'
print(str1)
print(str2)
print(str3)
print(type(str1))

# 三个双引号来定义字符串
str3 = """
Python可以用来做的事情
比如：
     可以用来做服务器开发
     可以做客户端开发
     可以做大数据处理
     可以做运维
     可以坐AI处理
"""
print(str3)

# 三个单引号来表示定义字符串
str4 = '''
Python可以用来做的事情
比如：\n
     可以用来做服务器开发
     可以做客户端开发
     可以做大数据处理
     可以做运维
     可以坐AI处理
'''
print(str4)
# 字符串这么多定义 到底有什么不一样
# 转义字符 单引号' 双引号"  \n 回车换行
# 如何知道字符串长度
str1 = "我爱你Python"
# len是系统的一个函数 表示返回长度
# 无论是汉字还是字母 都表示一个长度
# 不是表示内存和字节 是表示有几个字符（包括汉字）
# 编码Unicode 所有的字符都是2个字节 在计算机里面是16bits
# bit 叫做“位”或者“比特”是计算机信息的最小单位
# byte 叫做“字节” 是计算机文件容量大小的基本单位
# 其中 1byte=8bit A=2bytes(英文A是2个字节) 我=2bytes(汉字同为2个字节)
# Unicode的缺点是每个字符都是2个字节，若文件全是英文就太占内存，则衍生出来了 UTF-8
# 编码UTF-8（可用于优化内存） 是可变长的Unicode 表示如果是字母那长度为1 汉字长度为2或者3
# Python就是UTF-8编码  Python3默认是utf8
c = len(str1)
print(c)

# 把str1里面的第0个字符取出来  编号index是从0开始的
print("str1[0]", str1[0])

# 表示把字符串里面第一个到第五个之前的都取出来，记住字符是从0开始的
print("s", str1[1:5])

# 表示把字符串从开始第0个到第五个之前的取出来
print("s", str1[:5])

# 表示把字符串里面第二个开始到最后一个都取出来
print("s", str1[2:])

# 把字符串里面的都取出来
str2 = str1
print(str2)

# 把字符串从倒数第二个开始到最后
print('s', str1[-2:])
print('s', str1[-1:])

# 取字符串不要超过长度

# 字符串操作
str1 = 'hello'
str2 = 'world'
str3 = str1+str2
print(str3)
# *2表示 把字符串str1重新复制了一份
str3 = str1*2
print(str3)

# 字符串的 in/in not 操作
str1 = 'hello'
# in表示是否在里面 表示h字符是否在str1里面
c = 'h' in str1
print(c)
c = 'p' in str1
print(c)
# 表示p不在str1里面
c = 'p' not in str1
print(c)

# 整数 和 浮点数 和字符串的相互转换
age = '20'
# 把age字符串转化为int
ageint = int(age)
print(ageint, type(ageint))
age = '20.5'
agefloat = float(age)
print(agefloat, type(agefloat))

# 把int/float转成字符串
ageint = 100
agefloat = 10.33
# str函数表示把里面的内容转换为字符串
ageintstr = str(100)
agefloatstr = str(agefloat)
print(ageintstr, agefloatstr)
print(type(ageintstr), type(agefloatstr))

# format 格式化输出
name = "小明"
age = 20
# 把name字符串放在%s里面 把age放在%d里面 %s表示任意类型 包括字符串 %d表示整数
print('我叫 %s 今年 %d岁' % (name, age))
# age是整数 在这里要换为字符串
print('我叫' + name + '今年'+str(age)+'岁')

