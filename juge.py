# -*- coding: UTF-8 -*- 
# File Name: juge.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年03月23日 星期三 20时33分32秒
#########################################################################
#!/usr/bin/env python

def circle(f,t,i):
    return  [x for x in range(f,t+1,i)]
def isprinme(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            return False
        count -= 1
    else:
        return True

def getfactors(num):
    count = num / 2
    factors = []
    while count > 1:
        if num % count == 0:
            factors.append(count)
        count -= 1
    factors.append(num)
    factors.append(1)
    return factors

def defactors(num):
    result = []
    count = num 
    while count != 1:
        for x in getfactors(count):
            if isprinme(x):
                result.append(x)
                count /= x
                break
    return result

def sumnum(num):
    l = getfactors(num)
    l.remove(num)
    if num  == sum(l):
        return True
    else:
        return False

def factorial(num):
    result = 1;
    for x in range(1,num+1):
        result *= x
    return result

def fmnq(num):
    a = 1
    b = 1
    for x in range(num-2):
        a,b = b,a+b
    return b

def staticwords(thestr):
    l = thestr.split(' ')
    a = 'a'
    cw = 0
    ca = 0
    cw = len(l)
    for x in l:
        if a in x:
            ca += 1
    return cw,ca

def checkname():
    namecount = int(raw_input('Enter total number of names:'))
    i = 0
    cw = 0
    nl = []
    while i <namecount :
        name = raw_input('Please enter name %d:' % (i))
        if len(name.split(',')) != 2:
            cw += 1
            print 'Wrong format... should be last,first'
            print 'You have done this %d times already.Fixing input...' % (cw)
        else:
            nl.append(name)
            i +=1
    nl.sort()
    print 'The sorted list (by last name  ) is:'
    for x in nl:
        print x

def getnuminfo(first,last):
    print 'Begin:%d' % first
    print 'End %d' % last
    if first not  in range(33,255) and last not in range(33,255):
        print '%6s %6s %6s %6s' % ('DEC','BIN','OCT','HEX')
        print 20 * '-'
        for x in range(first,last+1):
            print '%6d %6s %6s %6s ' % (x,bin(x),oct(x),hex(x))
    else:
        print '%6s %6s %6s %6s %6s' % ('DEC','BIN','OCT','HEX','ASCII')
        print 20 * '-'
        for x in range(first,last+1):
            if x in range(33,255):
                print '%6d %6s %6s %6s %6s' % (x,bin(x),oct(x),hex(x),chr(x))
            else:
                print '%6d %6s %6s %6s' % (x,bin(x),oct(x),hex(x))
getnuminfo(26,41)
#checkname()
#test = 'hello wolrd i am the atest'
#print test
#print staticwords(test)
#print isprinme(7)

#print circle(2,10,2)

#print getfactors(15)

#print sumnum(6)

#print [x for x in range(200) if sumnum(x)]

#print factorial(3)

#print fmnq(1)


