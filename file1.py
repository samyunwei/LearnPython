# -*-coding:utf-8 -*-
# File Name: file.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
def checkfile():
    filename = raw_input('please input filename:\n')
    with open(filename,'r') as f:
        count = 0
        for eachline in f:
            count += 1
            if(count % 25 == 0):
                raw_input('Enter any key to contiue:\n')
            print '%5d' % (count),eachline.strip()

#checkfile()

def checkmarks():
    result = []
    while(True):
        filename = raw_input('please input filename:\n')
        if(filename == '.'):
            break
        else:
            with open(filename,'r') as f:
                for eachline in f:
                    if(eachline.strip() != ''):
                        result.append(int(eachline.strip()))
    return sum(result) // len(result)

print checkmarks()
        
