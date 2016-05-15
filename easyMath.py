# -*- coding: UTF-8 -*- 
# File Name: easyMath.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年04月27日 星期三 00时05分06秒
#########################################################################
#!/usr/bin/env python
from operator import add,sub,mul,div
from random import randint,choice

ops = {'+':add,'-':sub,'*':mul,'/':div}

MAXTRIES = 2

def doprob():
    op = choice('+-*/')
    nums = []
    if op != '/':
        nums = [randint(1,10) for i in range(2)]
        nums.sort(reverse=True)
    else:
        a = randint(1,10)
        if a != 1:
            b = choice([x for x in range(1,a+1) if (a % x == 0)])
        else:
            b = 1
        nums = [a,b]
    ans = ops[op](*nums)
    pr = '%d %s %d = ' % (nums[0],op,nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct'
                break
            if oops == MAXTRIES:
                print 'answer\n%s%d'%(pr,ans)
            else:
                print 'incorrect... try again'
                oops += 1
        except (KeyboardInterrupt,EOFError,ValueError):
            print 'Invail input ...try again'


def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again ?[y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt,EOFError):
            break

if __name__ == '__main__':
    main()


