# -*- coding: UTF-8 -*- 
# File Name: testfunc.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年04月21日 星期四 22时54分39秒
#########################################################################
#!/usr/bin/env python
from operator import add,mul
from functools import partial

#add1 = partial(add,1)
#mul100 = partial(mul,100)
#
#print add1(10)
#import Tkinter

#root = Tkinter.Tk()
#
#MyButton = partial(Tkinter.Button,root,fg='white',bg='blue')
#b1 = MyButton(text='Button1')
#b2 = MyButton(text='Button2')
#
#qb = MyButton(text='Quit',bg='red',command=root.quit)
#
#b1.back()
#b2.back()
#qb.back(fill = Tkinter.X,expand = True)
#root = title('PFAs!')
#root.mainloop()
#j ,k = 1,2
#def proc1():
#    j,k = 3,4
#    print 'j == %d and k == %d ' % (j,k)
#    k = 5
#
#def proc2():
#    j = 6
#    proc1()
#    print 'j == %d and k == %d ' % (j,k)
#
#k =  7
#proc1()
#print 'j == %d and k == %d ' % (j,k)
#
#j = 8
#proc2()
#print 'j == %d and k == %d ' % (j,k)

#####from random import randint
#####
#####def randGen(aList):
#####    while len(aList) > 0:
#####        yield aList.pop(randint(0,len(aList)-1))
#####
#####theList = ['rock','paper','scissors']
#####
#####for item in randGen(theList):
#####    print item
#####else:
#####    print theList
#def Fnums(themax,thefront = 1,therear = 2,count = 2):
#    if themax < 1:
#        return 'value error'
#    elif themax == 1:
#        return thefront
#    elif themax == 2:
#        return therear
#    elif count == themax:
#        return therear
#    else:
#        return Fnums(themax,therear,thefront + therear,count+1)
#for i in range(1,10):
#    print Fnums(i)
def myprintstr(thestr,thefrontindex = 0,thebackindex=-1):
    try:
        a,b = thestr[thefrontindex],thestr[thebackindex]
        print 'front',a,'back',b
        return myprintstr(thestr,thefrontindex+1,thebackindex-1)
    except IndexError,e:
        print 'finish'


myprintstr('abc')

