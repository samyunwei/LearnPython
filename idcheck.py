# -*- coding: UTF-8 -*- 
# File Name: idcheck.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年03月07日 星期一 19时57分31秒
#########################################################################
#!/usr/bin/env python
import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'

myInput = raw_input('Identifier to Test?')

if len(myInput) > 1 :
    if myInput[0] not in alphas:
        print '''incalid: first symbol must be 
        alphabetic'''
    else:
        for otherchar in myInput[1:]:
            if otherchar not in alphas + nums:
                print '''invalid:remaining 
                        symbol must be alphanumbetic'''
                break
        else:
            print 'okay as an identifier'
