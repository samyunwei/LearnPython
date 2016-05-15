# -*- coding: UTF-8 -*- 
# File Name: ll.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年03月09日 星期三 19时18分02秒
#########################################################################
#!/usr/bin/env python
def checkmark(marks):
    if not isinstance(marks,list):
        return 'marks Error'
    else:
        mark =  float(sum(marks))/len(marks)
        if mark >= 90:
            return 'A'
        elif mark >= 80:
            return 'B'
        elif mark >= 70:
            return 'C'
        elif mark >= 60:
            return 'D'
        else:
            return 'F'
##l = [100,80,90,90]
#print checkmark(l)

def getfl(thestr):
    for i in range(len(thestr)):
        print thestr[i],"   ",thestr[-i-1]
        
#getfl("hello")
def mycmp(astr,bstr):
    a,b = len(astr),len(bstr)
    if a != b:
        return False
    for i in range(a):
        if astr[i] != bstr[i]:
            return False
    else:
        return True

#print mycmp('hellO','hello')
def myrcmp(astr,bstr):
    a,b = len(astr),len(bstr)
    if a != b:
        return False
    for i in range(a):
        if astr[i] != bstr[-i-1]:
            return False
    else:
        return True

#print myrcmp('ollhh','hello')

def getrstr(thestr):
    return thestr + thestr[::-1]

#print getrstr("hello")

def mystrip(thestr):
    thestrlen = len(thestr)
    begl,endl = 0,0
    for i in range(thestrlen):
        if thestr[i] == ' ':
            begl += 1
        else:
            break
    for i in range(thestrlen):
        if thestr[-i - 1] == ' ':
            endl += 1 
        else:
            break
    return thestr[begl:thestrlen-1-endl]

print mystrip('hello                 '),'test','test'
print mystrip(' hello          ')
print mystrip('              hello')
