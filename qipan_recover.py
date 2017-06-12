# coding utf8
# python3
# 题目：翻转后的棋盘
#   在 4×4 的棋盘上摆满了黑白棋子，黑白两色的位置和数目随机
#   其中，左上角坐标为 (1,1)，右下角坐标为 (4,4)
#   现在依次有一些翻转操作，要对一些给定支点坐标为中心的上下左右四个棋子的颜色进行翻作
# 请计算出翻转后的棋盘颜色

# 给定两个数组 A和f 分别为初始棋盘和翻转位置。
# 其中翻转位置共有3个

# python qipan_recover.py -A \[\[0,0,1,1\],\[1,0,1,0\],\[0,1,1,0\],\[0,0,1,0\]\] -f \[\[2,2\],\[3,3\],\[4,4\]\]

import sys, getopt

def resover(status, station):
    x = station[0] - 1
    y = station[1] - 1
    if x - 1 >= 0:
        if status[x-1][y] == 0:
            status[x-1][y] = 1
        else:
            status[x-1][y] = 0
    if x + 1 < 4:
        if status[x+1][y] == 0:
            status[x+1][y] = 1
        else:
            status[x+1][y] = 0
    if y - 1 >= 0:
        if status[x][y-1] == 0:
            status[x][y-1] = 1
        else:
            status[x][y-1] = 0
    if y + 1 < 4:
        if status[x][y+1] == 0:
            status[x][y+1] = 1
        else:
            status[x][y+1] = 0
    return status


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "A:f:")
    for op, value in opts:
        if op == "-A":
            start_status = eval(value)
        elif op == "-f":
            station = eval(value)
    print(start_status)
    print(station)
    for s in station:
        start_status = resover(start_status, s)
    print (start_status)