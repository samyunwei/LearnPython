# -*-coding:utf-8 -*-
# File Name: test.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python

#'makeTestfile.py -- create text file'
import os
ls = os.linesep

#get file
fname = raw_input('Pleae input filename:')
while True:
    if os.path.exists(fname):
        print "Error: '%s' already exits" %fname
    else:
        break

#get file content (text)lines:
all = []

print "\nEnter lines ('.' by itself to quit).\n"

#loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'Done!'
