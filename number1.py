# -*-coding:utf-8 -*-
# File Name: number.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
def multi(a,b):
    return a*b

def checkmark(themark):
    if 90 <= themark <= 100:
        return 'A'
    elif 80 <= themark <= 89:
        return 'B'
    elif 70 <= themark <= 79:
        return 'C'
    elif 60 <= themark <= 69:
        return 'D'
    else:
        return 'F'
def checkyear(theyear):
    if not bool(theyear % 4) and  bool(theyear % 100):
        return True
    elif not(theyear % 400):
        return True
    else:
        return False
def checkcoins(thecoins):
    l = []
    for dev in (25,10,5,1):
        c = thecoins / dev
        l.append(c)
        thecoins -= c*dev 
    return l
def calcstr(thestr):
    for op in ['+','-','*','/','%']:
        l = thestr.split(op)
        if len(l) > 0:
            break
    if op == '+':
        temp = float(l[0]) + float(l[1])
    elif op == '-':
        temp = float(l[0]) - float(l[1])
#print checkmark(90)
#print checkyear(1700)
#print checkcoins(9)

#theyears = [x for x in range(1990,2016) if checkyear(x)]
#print theyears


