# -*-coding:utf-8 -*-
# File Name: catchThread.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
from myThread import MyThread
def catchstr(thestr,thecatch):
    return thestr.count(thecatch)

def catchsplit(thestr,splitcount):
    res = []
    count = len(thestr)
    beg = 0
    while True:
        if beg+splitcount < count: 
            temp = thestr[beg:beg+splitcount]
            res.append(temp)
            beg += splitcount
        else:
            res.append(thestr[beg:])
            break
    return res

def main():
    threads =[]
    
    thestr = 'dadadadadjadaldao;fhos;jclhsfojklvhadlvhalvna;j;vjadl;vva'

    strgoup = catchsplit(thestr,6)
    for eachitem in strgoup:
        t = MyThread(catchstr,(eachitem,'a'))
        threads.append(t)

    for eachthread in threads:
        eachthread.start()

    res = 0

    for eachthread in threads:
        eachthread.join()
        res += eachthread.getResult()

    print res

if __name__ == '__main__':
    main()
    
