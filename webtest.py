# -*-coding:utf-8 -*-
# File Name: tsTclnt.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
from socket import *

HOST = '192.168.1.1'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

tcpCliSock.sendall("GET/ HTTP/1.1\r\n\r\n")
html = tcpCliSock.recv(1024)
if html:
    print html
else:
    print 'None'
tcpCliSock.close()

