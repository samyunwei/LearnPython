# -*- coding: UTF-8 -*- 
# File Name: readNwriteTestFiles.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年03月01日 星期二 23时58分23秒
#########################################################################
#!/usr/bin/env python
import os
ls = os.linesep
def funwrite():
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
        fobj.writelines(['%s%s' % (x,ls) for x in all])
        fobj.close()
        print 'Done:'

def funcread():
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

model = raw_input('Please type model you want to choice w/r:\n')
if model == 'w':
    funwrite()
else:
    funcread()
