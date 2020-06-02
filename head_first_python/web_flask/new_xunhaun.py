# 求0--100内的奇数、偶数并求和
a = 0
sum_jishu = 0
sum_oushu = 0
while a < 101:
    if a % 2 == 0:
        print('%d是偶数' % (a))
        sum_oushu += a
    else:
        print("{}是奇数".format(a))
        sum_jishu += a
    a += 1
print("偶数只和是%s"%sum_oushu)
print("奇数之和是{}".format(sum_jishu))
