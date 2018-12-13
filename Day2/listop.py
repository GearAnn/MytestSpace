

# 我们来创建1个数组 然后操作
# 只是数组List的上半部分 之后的部分在后面讲

# 定义一个数组
lang = []
print(lang)
# 数组的长度 函数 就是 len(lang)空数组
print(len(lang))
# 查看lang是什么type
print(type(lang))

lang = ['c', 'c++', 'Java', 'Python', 'c#']
print(len(lang))
lang2 = ['Ruby', 'Perl', 'Bash']
# 把两个数组加在一起就是内容合并 然后赋值给新的数组lang3
# 数组后面追加 还有面向对象的方法 后续会处理
lang3 = lang + lang2
print(lang3)
# 取出第2项内容
print(lang[2])
# [:]表示取得数组里面的全部内容
print(lang[:])
# [Day12:3]表示从第1项取到第三项之前的内容
print(lang[1:3])

# 判断Python字符串是否在lang数组中
haselm = ('Python'in lang)
print(haselm)

# 修改元素
lang[1] = 'MS c++ 11'
print(lang)

# 删除lang里面第2项元素
del lang[2]
print(lang)

# 二维数组
row0 = [1, 2, 3]
row1 = [4, 5, 6]
row2 = [7, 8, 9]
matrix = [row0, row1, row2]

thisrow = matrix[2]
print(thisrow)
c = thisrow[1]
print(thisrow[1])
# 也可以这样一次性取元素
c = matrix[2][1]
print(c)
