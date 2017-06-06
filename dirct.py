# coding utf8
# python3
# python dirct.py -i \{1:\"我是\",2:\"是我\",3:\"你好\"\}

import sys, getopt
import os

dirct = {"我": "wo", "是":"shi", "你":"ni", "好":"hao"}

if __name__ == "__main__":

    opts, args = getopt.getopt(sys.argv[1:], "i:")
    for op, value in opts:
        if op == "-i":
            input = eval(value)
            break
    
    for k in input:
        a = input[k]
        b = ''
        for d in a:
            try:
                b = b+dirct[d]+' '
            except KeyError:
                print( "has no key: "+d)
        print( b ) 