# -*-coding:utf-8 -*-
# File Name: dicttest.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
import string
def socktest():
    stocks = []
    while(True):
        a = raw_input('hangqing:')
        name = raw_input('stockname')
        cp = float(raw_input('current price'))
        op = float(raw_input('old price'))
        if a == 'q':
            break
        l = [a,name,cp,op]
        stocks.append(l)
    choice = raw_input('please input your choice:n')
    result = {
            }
    if choice == 'n':
        stocks.sort(key=lambda x:x[1])
        print stocks
        for eachlist in stocks:
            result[eachlist[1]] = eachlist
    return result

def reversedict(a,b):
    tempa = a.copy()
    tempb = b.copy()
    a.clear()
    b.clear()
    for eachkey in tempb:
        a[tempb[eachkey]] = eachkey
    for eachkey in tempa:
        b[tempa[eachkey]] = eachkey

def hrs():
    db = {}
    while(True):
        name = raw_input('please input name:')
        number = raw_input('please input number:')
        if name == 'n':
            break
        db[name] = number
    templ =   db.keys()
    templ.sort()
    for eachkey in templ:
        print 'name:%s number:%s' % (eachkey,db[eachkey])
    print 'from numbers:'
    temp = list(db.items())
    temp.sort(key = lambda x:x[1])
    for eachkey in temp:
        print 'numbr:%s name: %s' % (eachkey[1],eachkey[0]) 

def tr(srcstr,dststr,string,flag):
    tempstr = string
    if flag:
        tempstr = string.lower()
        srcstr = srcstr.lower()
    l = tempstr.split(srcstr)
    result = ""
    i = 0
    for temp in l:
        if temp == '':
            result += dststr
            i += len(srcstr)
        else:
            result += string[i:i+len(temp)]
            i += len(temp)
    return result 

def rot13(thestr):
    result = ""
    small = string.letters[:13]+string.letters[26:39]
    big = string.letters[13:26]+string.letters[39:]
    for each in thestr:
        if each in small:
            result += chr(ord(each)+13)
        elif each in big:
            result += chr(ord(each)-13)
        else:
            result += each
    return result

#a ={1:'a'}
#b = {2:'b' }
#print a,b
#reversedict(a,b)
#print a,b

#print socktest()
#hrs()
#print tr('abcdef','mno','abcdefghiABCDef',False)

thestr = raw_input('Enter string to rot13:')
print 'Your string to encode was:',rot13(thestr)
