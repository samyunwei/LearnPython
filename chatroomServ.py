# -*-coding:utf-8 -*-
# File Name: tsUserv.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
from socket import *
from time import ctime
import thread
HOST = raw_input('Please type serv:')
if not HOST:
    HOST = '127.0.0.1'

PORT = raw_input('Please type PORT:')
if not PORT:
    PORT = 21567
else:
    PORT = int(PORT)
BUFSIZ = 1024

def Room1():
    ADDR = (HOST,PORT)
    udpSerSock = socket(AF_INET,SOCK_DGRAM)
    udpSerSock.bind(ADDR)
    users = []
    print 'Room 1 Start'
    while True:
        #print 'waiting for message...'
        data,addr = udpSerSock.recvfrom(BUFSIZ)
        if addr not in users:
            users.append(addr)
        for eachuseraddr in users:
            udpSerSock.sendto('[%s]: %s' % (addr,data),eachuseraddr)
        print '...recvived from and returned to:',addr
    udpSerSock.close()


def Room2():
    ADDR = (HOST,PORT+1)
    udpSerSock = socket(AF_INET,SOCK_DGRAM)
    udpSerSock.bind(ADDR)
    users = []
    print 'Room 2 Start'
    while True:
        #print 'waiting for message...'
        data,addr = udpSerSock.recvfrom(BUFSIZ)
        if addr not in users:
            users.append(addr)
        for eachuseraddr in users:
            udpSerSock.sendto('[%s]: %s' % (addr,data),eachuseraddr)
        print '...recvived from and returned to:',addr
    udpSerSock.close()

def main():
    thread.start_new_thread(Room1,())
    thread.start_new_thread(Room2,())

if __name__ == '__main__':
    main()
    while True:
        pass
    print 'main quit'
