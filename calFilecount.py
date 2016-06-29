# -*-coding:utf-8 -*-
# File Name: calFilecount.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
from myThread import MyThread
from Queue import Queue
from Queue import Empty
import os


def countlines(queue):
    totalcount = 0
    while True:
        try:
            thefile = queue.get(0)
            try:
                with open(thefile,'r') as f:
                    totalcount += len(f.readlines())
                    print totalcount
            except IOError,e:
                print e
        except Empty:
            break
    return totalcount


def Readfile(thedirpath):
    tempres = os.listdir(thedirpath)
    res = []
    for eachpath in tempres:
        if os.path.isfile(eachpath):
            res.append(eachpath)
    return res


def main():
    dirpath = raw_input('Please type theDirPath:\n')
    dirres = Readfile(dirpath)
    q = Queue(128) 
    for eachfile in dirres:
        q.put(eachfile,1)
    threads = []
    t1 = MyThread(countlines,(q,))
    t2 = MyThread(countlines,(q,))
    t3 = MyThread(countlines,(q,))
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    for eachthread in threads:
        eachthread.start()
    res = 0
    for eachthread in threads:
        eachthread.join()
        temp = eachthread.getResult()
        res += temp
    print 'AllDone Finish',res


if __name__ == '__main__':
    main()
    
