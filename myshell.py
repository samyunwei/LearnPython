# -*- coding: UTF-8 -*- 
# File Name: myshell.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年05月25日 星期三 23时33分12秒
#########################################################################
#!/usr/bin/env python
import os
def myexec(thecmd):
    f = os.popen(thecmd)
    theresult = []
    for eachline in f:
        eachline = eachline.strip()
        print eachline
        theresult.append(eachline)
    f.close() 
    return theresult

def RCmdPipe(thecmd):
    thecmdlist = []
    while len(thecmd):
        therlist = []
        thellist = []
        for i in range(len(thecmd)):
            if thecmd[i] == '(':
                thellist.append(i)
            if thecmd[i] == ')':
                therlist.append(i)
        if len(thellist) != len(therlist):
            raise TypeError('un experct )')
        bindex = 0
        eindex = -1
        if(len(thellist) != 0 and len(therlist) != 0):
            bindex = thellist.pop(-1)
            print therlist
            eindex = therlist.pop(0)
            thecmdlist.append(thecmd[bindex+1:eindex])
            thecmd = thecmd[:bindex]+thecmd[eindex+1:]
        else:
            thecmdlist.append(thecmd)
            thecmd = ""
        theres = ''
        lastcmd = []
        for eachcmd in thecmdlist:
            temp = eachcmd.split(',')
            theres += temp.pop(0)
            if len(lastcmd) != 0:
                for eachlastcmd in lastcmd:
                    theres += ' ' +eachlastcmd
            theres += '|'
            lastcmd = temp
        theres = theres[:-1]
        
    return theres








def run():
    while True:
        thecmd = raw_input('Please Type the cmd:')
        if thecmd == 'quit':
            break
        else:
            res = myexec(RCmdPipe(thecmd))
            for eachline in res:
                print eachline


if __name__ == '__main__':
    run()
