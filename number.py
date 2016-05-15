# -*- coding: UTF-8 -*- 
# File Name: number.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年03月06日 星期日 22时30分10秒
#########################################################################
#!/usr/bin/env python
from __future__ import division
import math
import re
def zfxs(a):
    return 6*a*a
def zfxv(a):
    return a**3
def lfts(a,b,c):
    return 2*(a*b+b*c+c*a)
def lftv(a,b,c):
    return a*b*c
def ballsquare(r):
    return 4.0*math.pi*r**2
def ballv(r):
    return 3/4.0*math.pi*r*3
def FTC(theF):
    return (theF - 32) / (5/9)
def geteven(themax):
    l = []
    for x in range(themax):
        if not x%2:
            l.append(x)
    return l
def getodd(themax):
    l = []
    for x in range(themax):
        if  x%2:
            l.append(x)
    return l
def justD(a,b):
    if a%b and b%a:
        return False
    else:
        return True
def mhtm(thestr):
    pattern = re.compile(r'^(\d+)h(\d+)m$')
    result = pattern.match(thestr)
    if result: 
        return float(result.group(1))*60+float(result.group(2))
    else:
        return "syntax error"
def bankm(p,d):
    result = 1
    for x in range(d):
        result = (1+p)*result
    return result-1
def calcmm(a,b):
    l = []
    result = a*b
    n = a%b
    while n:
        a = b
        b = n
        n = a % b
    l = []
    l.append(b)
    l.append(result/b)
    return l
def Payment():
    opening = float(raw_input('please input opening money:'))
    monthly = float(raw_input('please input monthly pay:'))
    print '%10s'%('Amount Remaining')
    print '%10s%10s%10s'%('Pymt#','Paid','Balance')
    print '%10s%10s%10s'%(5*'-',5*'-',10*'-')
    n = 0
    Paid = 0
    while opening:
        print '%10d $%9f $%9f'%(n,Paid,opening)
        if (opening - monthly)>=0:
            Paid = monthly
            opening -= monthly
        else:
            Paid = opening
            opening = 0
        n += 1
    
    print '%10d $%9f $%9f'%(n,Paid,opening)
#print ballsquare(2)
#print ballv(3)
#print zfxs(2)
#print zfxv(2)
#print lfts(2,3,4)
#print lftv(2,3,4)
#print FTC(45)
#print geteven(20)
#print getodd(20)
#print mhtm("333333")
#print bankm(0.1,2)
#print calcmm(15,5)
Payment()
