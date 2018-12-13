

# 程序都是从上到下执行
# Python的编程风格是 缩进风格 是Python独有的
# 因为必须顶格写 否则 IndentationError: unexpected indent ，缩进也是语法的一部分
# 同一层次必须对齐
#
age = 20
name = 'yang'
score = 99
print(name, age, score)

# 进入条件判断 ，if elif判断的是真和假,并且只会返回True,打印也只能打印出True
if age >= 18:
    # age>=18 返回是True
    # 这里2个print缩进对齐，是表示第二个print是在 if 这个条件语句下，属于同层次
    print('age大于18')
    print(name)
# 其他语言中 可能每一个层次会有个 end来结束 但是Python重新提行顶格就开始新的层次

age = 20
name = 'yang'
score = 99

if age > 18 and score > 80:
    print('age>18同时score>80')
else:
    print("条件不满足")
# 可以看到elif可以写无数个
age = 14
name = 'yang'
score = 99
if age > 18 and score > 80 and name == 'yang':
    print("的确是age>18 score>80 name==yang")
elif age > 16:
    print("年龄在16—18之间")
elif 13 < age <= 16:
    print("年龄在13-16之间")

# a不是一个bool变量  a是一个非0的数 ，Python系统认为非0就是True
# 牢记在几种特点情况下  Python会认为是 False，如下：
# None False 空的字符串 空的数组[] 空的元组() 空的字典{} 空的引号''""
# 除此之外都是True
# bool变量就只有True 和 False 两个

a = 5
if a:
    print('if a')
else:
    print('else')

list2 = ['yang', 'wang']
if 'yang' and 'wang' in list2:
    print('正确')

# 条件嵌套
a = 10
list2 = ['yang', 'wang']
if a:
    print('a')
    if 'yang' in list2:
        print('正确')
