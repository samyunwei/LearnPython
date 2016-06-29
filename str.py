# -*-coding:utf-8 -*-
# File Name: str.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
import string
import random
ndict = {
        0:'zero',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine'
        }

def getnstr(thenumber):
    tempstr = ndict[thenumber % 10]
    thenumber /= 10
    while(thenumber >= 10):
        tempstr = ndict[thenumber % 10]+'-'+tempstr 
        thenumber /= 10 
    if(thenumber != 0):
        tempstr = ndict[thenumber]+'-'+tempstr 
    return tempstr

#while(True):
#    thestr = int(raw_input('please input:'))
#    print getnstr(thestr) 
def gethm(them):
    return str(them / 60)+'h'+str(them % 60)+'m'

def rstr(thestr):
    therstr=""
    for c in thestr:
        if c in string.lowercase:
            therstr += c.upper()
        elif c in string.uppercase:
            therstr += c.lower()
        else:
            therstr += c
    return therstr
#print gethm(350)
#print rstr('Ee.Rr')
def IPINT(theInt):
    if isinstance(theInt,list):
        return str(theInt[3])+'.'+str(theInt[2])+'.'+str(theInt[1])+'.'+str(theInt[0])
        return tempstr
    if isinstance(theInt,str):
        return [int(x) for x in theInt.split('.')]

#print IPINT([1,1,1,1])
#print IPINT("111.111.111.111")
#print str(1)
def findchar(thestr,char):
    l = len(thestr)
    for i in range(l):
        if thestr[i] == char:
            return i
    else:
        return -1

#print findchar("123456","3")

def rfindchar(thestr,char):
    l = len(thestr)
    for i in range(l):
        if thestr[-i-1] == char:
            return l-i-1
    else:
        return -1

def subchar(thestr,origchar,newchar):
    l = len(thestr)
    tempstr = ""
    for i in range(l):
        if thestr[i] == origchar:
            tempstr += newchar
        else:
            tempstr += origchar
    return tempstr
#print rfindchar("123456","3")
#print subchar("333","3","2")

checkdict = {
        0:'loss',
        1:'tie',
        2:'win'
        }
def checkstack(P,C):
    print 'p:%d,c:%d' % (P,C)
    return checkdict[(P-C+4) % 3 ]

#while(True):
#    c = random.randint(1,3)
#    p = int(raw_input('Please input your choice:'))
#    print checkstack(p,c)
monthdays = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
        }

def checkyear(theyear):
    if not bool(theyear % 4) and  bool(theyear % 100):
        return True
    elif not(theyear % 400):
        return True
    else:
        return False


def getdays(str1,str2):
    l1 = str1.split('/')
    l2 = str2.split('/')
    y1,y2,m1,m2,d1,d2 = int(l1[0]),int(l2[0]),int(l1[1]),int(l2[1]),int(l1[2]),int(l2[2])
    thedays1 = 0
    for i in range(1970,y1):
        if checkyear(i):
            thedays1 += 366
        else:
            thedays1 += 365
    for i in range(1,m1):
        thedays1 += monthdays[i]
    for i in range(1,d1):
        thedays1 += 1
    thedays2 = 0
    for i in range(1970,y2):
        if checkyear(i):
            thedays2 += 366
        else:
            thedays2 += 365
    for i in range(1,m2):
        thedays2 += monthdays[i]
    for i in range(1,d2):
        thedays2 += 1

    return thedays1 - thedays2


#print getdays('2016/4/11','2013/3/8')

def martix(A,B):
    a = len(A)
    b = len(A[0])
    C = []
    for i in range(a):
        tl = []
        for j in range(b):
            tl.append(A[i][j]+B[i][j])
        C.append(tl)
    return C

def martixmu(A,B):
    a1 = len(A)
    a2 = len(A[0])
    b1 = len(B)
    b2 = len(B[0])
    C = []
    for i in range(b2):
        tl = []
        C.append(tl) 
    for i in range(a1):
        c = 0
        for j in range(a2):
            c += A[i][j]*B[j][i]
            C.append(c)
    return C
#A = [[1,2],[2,3],[1,1]]
#B = [[1,2],[1,1],[1,1]]

#print martix(A,B)
