# coding utf8
# python3
# 题目：完全平方数
#   一个整数，它加上100和加上268后都是一个完全平方数
# 求该数是多少
# 数字[1, 1000]中，符合条件的数：
#   python sqrt_num.py -b 1 -e 1000

import sys, getopt
import math

def int_num( begin, end ):

    for i in range(begin, end, -1 if begin>end else 1):
        x = int(math.sqrt(i+100))
        y = int(math.sqrt(i+268))
        if x*x == i+100 and y*y ==i+268:
            print( i )

if __name__ == "__main__":
    begin = 1
    end = 100
    opts, args = getopt.getopt( sys.argv[1:], "b:e:" )
    for op, value in opts:
        if op == "-b":
            begin = int(value)
        elif op == "-e":
            end = int(value)
        
    print("在区间 [%d, %d] 中，符合条件的数有：" %(begin,end))

    int_num(begin, end)