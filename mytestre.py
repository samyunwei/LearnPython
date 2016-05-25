# -*- coding: UTF-8 -*- 
# File Name: mytestre.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年05月25日 星期三 23时48分27秒
#########################################################################
#!/usr/bin/env python
import re

teststr = 'sort(grep(ps -ef,root),-n)'
teststr2 = '(111)'
restr = r'\(.+\)'

myre = re.compile(restr)

res =  myre.findall(teststr)
if res:
    for eachitem in res:
        print eachitem
else:
    print 'No match'
