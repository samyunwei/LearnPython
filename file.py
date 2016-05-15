# -*- coding: UTF-8 -*- 
# File Name: file.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年04月07日 星期四 23时57分37秒
#########################################################################
#!/usr/bin/env python
import os
import codecs
def checklib():
    mylibpath = '/usr/lib/python2.7/'
    os.chdir(mylibpath)
    cwd = os.getcwd()
    l = os.listdir(cwd)
    lpy = []
    result = []
    for everfile in l:
        if '.py' in everfile:
            lpy.append(everfile)
    for everfile in lpy:
        with open(everfile,'r') as f:
            count = 0
            for everline in f:
                count += 1
                if '_doc_' in everline:
                    result.append((everfile,count,everline))
                   # print(everline)
                    break
    
    os.chdir('/home/sam/桌面/LearnPython')
    with open('docresult.txt','w') as f:
        for everresult in result:
            f.write('filename:'+everresult[0]+'row:'+str(everresult[1])+'\n')
        for everfile in lpy:
            if everfile not in result:
                f.write('do not have doc:'+everfile+'\n')

        
    
checklib()
