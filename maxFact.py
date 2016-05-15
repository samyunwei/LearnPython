# -*- coding: UTF-8 -*- 
# File Name: maxFact.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年03月21日 星期一 22时38分09秒
#########################################################################
#!/usr/bin/env python
def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print 'largest factor of %d is %d' % (num,count)
            break
        count -= 1
    else:
        print num, 'is prime'

for eachnum in range(10,21):
    showMaxFactor(eachnum)
