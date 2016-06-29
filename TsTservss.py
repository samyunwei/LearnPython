# -*-coding:utf-8 -*-
# File Name: TsTservss.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
from SocketServer import (TCPServer as TCP,StreamRequestHandler as SRH)
from SocketServer import ForkingTCPServer
from time import ctime


HOST = '127.0.0.1'
PORT = 6666
ADDR = (HOST,PORT)

class MyRequsetHandler(SRH):
    def handle(self):
        while True:
            #print '...connected from:',self.client_address
            theline = self.rfile.readline()
            res = theline.strip()
            if res != 'quit':
                if theline:
                    self.wfile.write('[%s] %s' % (ctime(),theline))
            else:
                break




tcpServ = ForkingTCPServer(ADDR,MyRequsetHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
