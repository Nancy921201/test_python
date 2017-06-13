/************************
* 有一个由大小写组成的字符串，现在需要对他进行修改
* 将其中的所有小写字母排在大写字母之前
* 大小写的字母之间不要求保持原来的次序
* 如有可能尽量选择时间和空间效率高的算法
*************************/

#include<stdio.h>
#include<string.h>

void proc(char *str){
    int len = strlen(str);
    int i = 0, j = len-1;
    char a, b;
    int small = 0;
    int big = 0;
    do{
        small = 0;
        big = 0;
        a = str[i];
        b = str[j];
        if( a >= 'a' && a <= 'z' ){
            i = i+1;
            small = 1;
        }
        if( b >= 'A' && b <= 'Z' ){
            j = j-1;
            big = 1;
        }
        if( small == 0 && big == 0 ){
            str[i] = b;
            str[j] = a;
            i = i+1;
            j = j-1;
        }
    }while(i!=j);
}

void main(void){
    char str[128];
    printf("输入需要改变顺序的字符串：");
    scanf("%s", str);
    proc( str );
    printf( "顺序修改之后：%s\n", str);
}