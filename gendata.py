# -*-coding:utf-8 -*-
# File Name: gendata.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
from random import randint ,choice
from string import lowercase
from sys import maxint
from time import ctime

doms = ('com','edu','net','org','gov')
res = []
for i in range(randint(5,10)):
    dtint = randint(0,maxint-1)
    dtstr = ctime(dtint)

    shorter = randint(4,7)
    em = ''
    for j in range(shorter):
        em += choice(lowercase)

    longer = randint(shorter,12)

    dn = ''

    for j in range(longer):
        dn += choice(lowercase)

    tempstr = '%s::%s@%s.%s::%d-%d-%d' % (dtstr,em,dn,choice(doms),dtint,shorter,longer)
    res.append(tempstr)

try:
    with open('redata.txt','w') as f:
        for eachline in res:
            f.write(eachline+'\n')
except IOError,e:
    print e

