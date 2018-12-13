
# 输出9x9乘法表 用for in

for num in range(1, 10):
    for j in range(1, num + 1):
        c = num * j
        print("%d * %d = %d" % (num, j, c), end='   ')
    print('')
