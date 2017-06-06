# coding utf8
# python3
# python print_cv.py -v "3 1" 
# python print_cv.py -c "1 3" 

import sys
import sys, getopt 

text = {3:"我是", 1:"是我", 2:"你好"}

def cun( key ):
    for k in key:
        try:
            print(text[k])
        except KeyError:  
            print ("has no key: " + k ) 

def vaild( key):
    text_keys = sorted(text.keys())
    key_sort = sorted(key)
    j = 0
    k = int(key_sort[j])
    for i in text_keys:
        if i == k or i>k:
            j = j + 1
            if j<len(key_sort):
                k = int(key_sort[j])
        else:
            print(text[i])

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "v:c:")
    for op, value in opts:
        if op == "-v":
            key = [int(x) for x in value.split()]
            key1 = sorted(key)
            vaild( key )
        elif op == "-c":
            key = [int(x) for x in value.split()]
            cun(key)