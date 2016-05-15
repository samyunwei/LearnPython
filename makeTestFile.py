# -*- coding: UTF-8 -*- 
# File Name: makeTestFile.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年03月01日 星期二 23时04分44秒
#########################################################################
#!/usr/bin/env python
import os
ls = os.linesep
#while True:
#    fname = raw_input('Enter filename:')
#    if os.path.exists(fname):
#        print "Error: '%s' already exists" % fname
#    else:
#        break
fname = raw_input('Please input fname')
try:
    fobj = open(fname,'w')
except IOError,e:
    print "FIle open Error :",e
else:
    all = []
    print "\nEnter line ('.' by itself to quit). \n"
    while True:
        entry = raw_input('>')
        if entry == '.':
            break
        else:
            all.append(entry)
#fobj = open(fname,'w')
    fobj.writelines(['%s%s' % (x,ls) for x in all])
    fobj.close()
    print 'Done:'
