# -*-coding:utf-8 -*-
# File Name: tsTserv.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
from socket import *
from time import ctime
from time import sleep
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

tcpRegSock = socket(AF_INET,SOCK_STREAM)
tcpRegSock.connect(('127.0.0.1',6666))
tcpRegSock.send('reg:test1'+':'+HOST+':'+str(PORT))
data = tcpRegSock.recv(BUFSIZ)
print data
tcpRegSock.close()
while True:
    print 'waiting for connection...'
    tcpCliSock,addr = tcpSerSock.accept()
    print '...Connected...from:',addr
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        if data != 'wait':
            tcpCliSock.send('[%s] %s' % (ctime(),data))
        else:
            sleep(3)
            tcpCliSock.send('sleep finish!')

    tcpCliSock.close()

tcpSerSock.close()

