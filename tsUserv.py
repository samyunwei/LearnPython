# -*-coding:utf-8 -*-
# File Name: tsUserv.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
from socket import *
from time import ctime

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


udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data,addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s' % (ctime(),data),addr)
    print '...recvived from and returned to:',addr

udpSerSock.close()



