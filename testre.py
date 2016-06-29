# -*-coding:utf-8 -*-
# File Name: testre.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
import re
from time import ctime
def readfile():
    resl = []
    try:
        with open('redata.txt','r') as f:
            for eachline in f:
                resl.append(eachline.strip())
    except IOError,e:
        print e
    finally:
        return resl

def staticMonth(ml):
    res = []
    for eachItem in ml:
        if len(res) == 0:
            res.append((eachItem,1))
        else:
            for i in range(len(res)):
                if res[i][0] == eachItem:
                    res[i] = (res[i][0],res[i][1]+1)
                    break
            else:
                res.append((eachItem,1))
    return res
data = 'epgvy@qhucf.gov::1098049880-5-5'
#patt = '.+?(\d+-\d+-\d+)'
#data = 'bat'
#patt = 'bat|bit|but|hat|hit|hut'
#data = 'hello world'
#patt = r'(\b\w+)\s(\b\w+)'
#data = '_str'
#patt = '^(\w|_)([\w\d_]+)'
#data = '212 da dd ddd ddd ddd'
#patt = '([\w\d]+\s?)+'
#data = 'www.yahoo.com'
#patt = 'www\.[\w\d]+\.com|net|edu'
#data = '111111111'
#patt = '\d{0,32}'
#data = '12.32'
#patt = '\d+\.\d+'
#data = '23+2i'
#patt = '(\d+)[+-](\d+i)'
#data = 'nobody@www.xxx-yyy.zzz.com'
#patt = '\w+@([\w-]+\.)*\w+\.com'
#data = 'www.xxx-yyy.zzz.edu'
#patt = 'www\.([\w-]+\.)*\w+\.(\w+)'
#data  = str(type('sssss'))
#patt = "<type\s'(\w+)'>"
#data = '12'
#patt = '^0?[0-9]$|^1[0-2]$'
#data = '111-111111-11111'
#data2 = '1111-1111-1111-1111'
#patt = '^[0-9]{3}-[0-9]{6}-[0-9]{5}$|^\d{4}-\d{4}-\d{4}-\d{4}$'
resl = readfile()
ml = []
for eachline in resl:
    data = eachline
    #print data
    #patt = r'(.+)(::\w+@)'
    #patt = r'::'
    #patt = r'\w+@\w+\.\w+'
    #patt2 = '^\d+'
    patt = r'\b\d{4}'
    myre = re.compile(patt)
    res = myre.search(data)
    if res is not None:
        ml.append(res.group().replace(' ',''))
        #if res[0] != ctime(int(re.search(patt2,res[2]).group())):
            #print 'line Error!'
        #else:
            #print 'line right'
        #print res.group()

staticres = staticMonth(ml)
for eachItem in staticres:
    print eachItem
