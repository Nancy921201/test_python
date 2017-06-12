# coding utf8
# python3
# 题目：1 的个数
#   给定一个十进制整数 N，求出从 1 到 N 的所有整数中出现 “1” 的个数

# 当 N=12 时，
#   python num_of_1.py -N 12

import sys, getopt

def sum_num(n):
    if n == 0:
        return 0
    elif n < 10:
        return 1
    
    num = 0
    c1 = 10
    c2 = 1

    a = int(n/c1)
    b = n%c1
    if b == 0:
        num = num + a
    else:
        num = num + a + 1

    while (a > 0):
        c2 = c1
        c1 = c1*10
        a = int(n/c1)
        b = int((n%c1)/c2)
        c = (n%c1)%c2
        if b == 0:
            num = num + a*c2
        elif b == 1:
            num = num + a*c2 + c+1
        else:
            num = num + (a+1)*c2

    return num


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "N:")
    for op, value in opts:
        if op == "-N":
            n = int(value)
            break
    
    num = sum_num(n)
    print("从 1 到 %d 的所有整数中出现 “1” 的个数为：%d" %(n, num))
