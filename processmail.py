# -*-coding:utf-8 -*-
# File Name: processmail.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
from Queue import Queue
from myThread import MyThread
import re

def catchemail(thestr):
    restr = r'\w+@\w+\.com'
    myre = re.compile(restr)
    res = myre.findall(thestr)
    return res

def ReadFile(thefile,queue):
    try:
        with open(thefile,'r') as f:
            for eachline in f:
                emails = catchemail(eachline.strip())
                for eachmail in emails:
                    try:
                        queue.put(eachmail,1)
                    except Queue.Full:
                        Queue.sleep(1)
            queue.put('quit',1)
    except IOError,e:
        print e

def WriteFile(thefile,queue):
    try:
        with open(thefile,'w') as f:
            while True:
                try:
                    theline = queue.get(1)
                    if theline == 'quit':
                        break
                    else:
                        f.write(theline+'\n')
                except Queue.Empty,e:
                    Queue.sleep(1)
    except IOError,e:
        print e
            


def main():
    threads = []
    q = Queue(128)

    Rt = MyThread(ReadFile,('emails.txt',q))
    Wt = MyThread(WriteFile,('mails.html',q))

    threads.append(Rt)
    threads.append(Wt)
    print 'start ..'
    for eachthread in threads:
        eachthread.start()

    for eachthread in threads:
        eachthread.join()

    print 'All Done'

if __name__ == '__main__':
    main()
