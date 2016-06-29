# -*-coding:utf-8 -*-
# File Name: tsTclnt.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
from socket import *

HOST = '127.0.0.1'
PORT = 6666
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpGetSock = socket(AF_INET,SOCK_STREAM)
tcpGetSock.connect(ADDR)
tcpGetSock.send('get:test1')
ADDR = tcpGetSock.recv(BUFSIZ)
ADDR = ADDR.split(':')
ADDR = (ADDR[0],int(ADDR[1]))
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('>')
    if not data:
        break
    tcpCliSock.sendall(data)
    print tcpCliSock.gettimeout()
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data

tcpCliSock.close()

