# -*- coding: UTF-8 -*- 
# File Name: readTextFile.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年03月01日 星期二 22时04分39秒
#########################################################################
#!/usr/bin/env python
import os
ls = os.linesep
#fname = raw_input('Enter filename:')

#try:
#    fobj = open(fname,'r')
#except IOError,e:
#    print "FIle open Error :",e
#else:
#    for eachLine in fobj:
#        print eachLine
#    fobj.close()

while True:
    fname = raw_input('Enter filename:')
    if os.path.exists(fname):
        break
    else:
        print "Error: '%s' not exists" % fname
fobj = open(fname,'r')
for eachLine in fobj:
    print eachLine.strip()
fobj.close()
