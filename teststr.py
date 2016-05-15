# -*- coding: UTF-8 -*- 
# File Name: teststr.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年03月10日 星期四 22时39分56秒
#########################################################################
#!/usr/bin/env pytho
def atoc(thestr):
    a = ''
    b = ''
    l = len(thestr)
    i = 0
    while i < l:
        if (thestr[-i-1] != '+' and  thestr[-i-1] != '-'):
            i += 1
        elif thestr[-i-2] == 'e':
            i+=1
        else:
            break
    return complex(float(thestr[:-i-1]),float(thestr[-i-1:-1]))

print atoc('13+4j')



