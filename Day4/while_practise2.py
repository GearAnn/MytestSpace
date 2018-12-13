
# 计算矩阵Matrix相加3x3
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[7, 9, 8], [1, 5, 0], [6, 4, 3]]
c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# a + b --> c
# 先算第0行的数据
row = 0
column = 0
while column < 3:
    c[row][column] = a[row][column] + b[row][column]
    column += 1
print(c)

# 完全计算所有的 row 算出矩阵值
row = 0
column = 0
while column < 3:
    c[row][column] = a[row][column] + b[row][column]
    column += 1
row = 1
column = 0
while column < 3:
    c[row][column] = a[row][column] + b[row][column]
    column += 1

row = 2
column = 0
while column < 3:
    c[row][column] = a[row][column] + b[row][column]
    column += 1
print(c)

# 这个时候就使用循环 来避免重复操作 同时也是循环的嵌套
column = 0
row = 0
while row < 3:
    # 下面的代码就是计算第row行 第0，Day12，2 column
    while column < 3:
        c[row][column] = a[row][column] + b[row][column]
        column += 1
    row += 1
print(c)

# Matrix的乘法 a * b = c
# 算法Matrix的乘法规则是 c00 = a00 * b00 + a01 * b10 + a02 * b20
# 思路：首先把计算过程分阶段
# 先算 第0行 第0列的数据
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[7, 9, 8], [1, 5, 0], [6, 4, 3]]
row = 0
column = 0
msum = 0
k = 0
while k < 3:
    # a00 * b00 + a01 * b10 + a02 * b20 其中a的行数 b的列没有变 所以先把行给定下来
    msum += a[row][k] * b[k][column]
    k += 1
print(msum)
# 所以说上面的代码是用来算 的某行某列项 的单一结果 不是整个矩阵

# 现在计算所有行列的所有数据
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[7, 9, 8], [1, 5, 0], [6, 4, 3]]
row = 0
while row < 3:
    column = 0
    msum = 0
    k = 0
    while column < 3:
        msum = 0
        k = 0
        # 下面的程序就是算出了 某行某列的值
        while k < 3:
            msum += a[row][k] * b[k][column]
            k += 1
        print(msum)
        c[row][column] = msum
        column += 1
    row += 1
print(c)
# 从上面就可以看出来 循环 我们需要把复杂的东西分成每一步来碎片化
# 然后计算每一小步，最后再合起来












