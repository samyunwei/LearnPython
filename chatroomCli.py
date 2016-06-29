# -*-coding:utf-8 -*-
# File Name: tsUclnt.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python

from socket import *
import thread
import sys

HOST = '127.0.0.1'
PORT = int(raw_input('Please Type Port:'))
BUFSIZ = 1024
ADDR = (HOST,PORT)


def loop(thesocket):
    while True:
        data,ADDR = thesocket.recvfrom(BUFSIZ)
        if data == 'quit!':
            break
        print data
        sys.stdout.flush()

def main():
    udpCliSock = socket(AF_INET,SOCK_DGRAM)
    if(udpCliSock):
        thread.start_new_thread(loop,(udpCliSock,))
    while True:
        sys.stdout.flush()
        data = raw_input()
        if not data:
            break
        udpCliSock.sendto(data,ADDR)
    udpCliSock.close()

if __name__ == '__main__':
    main()
