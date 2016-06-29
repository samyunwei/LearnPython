# -*-coding:utf-8 -*-
# File Name: buggy.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python

#get str
num_str = raw_input('Enter a number')

#str to num
num_num = int(num_str)

#
fac_list = range(1,num_num+1)
print 'BEFORE:',fac_list

#get %list
i = 0
#find list
while i < len(fac_list):
    print fac_list[i]
    if num_num % fac_list[i] == 0:
        del fac_list[i]
        #else i+1
    else:
        i = i+1

print 'AFTER:',fac_list
