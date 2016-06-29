# -*-coding:utf-8 -*-
# File Name: tsTserv.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
from socket import *
import os
import thread
from time import ctime
from time import sleep
def writelog(thelog,thefile = './service.txt'):
    try:
        with open(thefile,'a') as f:
            f.write(thelog)

    except IOError,e:
        print e

def checkservice(theservices):
    while True:
        theclear = None
        for eachservice in theservices:
            f = os.popen('ping %s -c 3' % eachservice[1][0])
            f.readline()
            line = f.readline()
            print line
            if 'able' in line:
                eachservice[0].close()
                theclear = eachservice
                break
            f.close()
        if theclear:
            theservices.remove(theclear)
            print 'remove'
        print 'checkone'
        sleep(1)



HOST = raw_input('Please type serv:')
if not HOST:
    HOST = '127.0.0.1'

PORT = raw_input('Please type PORT:')
if not PORT:
    PORT = 21567
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

services = []
thread.start_new_thread(checkservice,(services,))
while True:
    print 'waiting for connection...'
    tcpCliSock,addr = tcpSerSock.accept()
    print '...Connected...from:',addr
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        data = data.split(':')
        if (len(data) != 4) and  (len(data) != 2):
            tcpCliSock.close()
            break
        if data[0] == 'reg':
            services.append((tcpCliSock,(data[2],data[3]),data[1]))
            tcpCliSock.send('regOK')
            thelog = str(data[0]) +  str(data[2]) + str(data[3]) + str(data[1]+ '\n')
            writelog(thelog)
            break
        if data[0] == 'get':
            for eachservice in services:
                if eachservice[2] == data[1]:
                    tcpCliSock.send(eachservice[1][0]+':'+eachservice[1][1])
                    thelog = str(addr) + data[0] + data[1] + '\n'
                    writelog(thelog)
                    break
                else:
                    tcpCliSock.send('None')
            tcpCliSock.close()
            break
        else:
            tcpCliSock.close()
            break

tcpSerSock.close()

