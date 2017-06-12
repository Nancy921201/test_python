# test_python

# dirct.py
    中文转化为拼音
    python dirct.py -i \{1:\"我是\",2:\"是我\",3:\"你好\"\}

# print_cv.py
    打印关键字的内容
    python print_cv.py -c "1 3"
    
    打印出去某些关键字的其他内容
    python print_cv.py -v "3 1"

# monkey.py
    猴子吃桃子的问题
    第10天吃之前剩下1个桃子： python monkey.py -n 10 -x 1

# sqrt_num.py
    完全平方数
    数字[1, 1000]中，符合条件的数：python sqrt_num.py -b 1 -e 1000

# box_open_or_close.py
    储物柜状态问题
    python box_open_or_close.py

# qipan_recover.py
    翻转后的棋盘
    初始棋盘状态为： [[0,0,1,1],[1,0,1,0],[0,1,1,0],[0,0,1,0]]
    翻转位置为： [[2,2],[3,3],[4,4]]
    python qipan_recover.py -A \[\[0,0,1,1\],\[1,0,1,0\],\[0,1,1,0\],\[0,0,1,0\]\] -f \[\[2,2\],\[3,3\],\[4,4\]\]