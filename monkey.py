# coding utf8
# python3
# 题目：一只猴子吃桃子的问题
#   一只猴子，第一天摘下若干个桃子，并吃了一半，感觉吃得不过瘾，然后又吃了一个。
#   第二天，又吃了剩下的一半零一个
#   以后每天早上，都吃前一天剩下的一半零一个
#   到了第 n 天，发现吃之前剩下了 x 个桃子
# 求猴子第一天总共摘了多少个桃子？
# 第10天吃之前剩下1个桃子：
#   python monkey.py -n 10 -x 1

import sys, getopt

def sum_num( day, num ):
    # 使用递归方式
    # 当第1000天的时候，内存溢出
    '''
    if day == 1:
        return num
    else:
        return sum_num( day-1, (num+1)*2 )
    '''
    # 使用循环方式
    for i in range(day,1,-1):
        num = (num + 1)*2
    return num

if __name__ == "__main__":
    opts, args = getopt.getopt( sys.argv[1:], "n:x:" )
    for op, value in opts:
        if op == "-n":
            day = int(value)
        elif op == "-x":
            num = int(value)

    print("第 %d 天吃之前剩下 %d 个桃子" %(day,num))
    num = sum_num( day, num )
    print("猴子第一天总共摘了 %d 个桃子" %num)