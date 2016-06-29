# -*-coding:utf-8 -*-
# File Name: tsTservTW.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
from twisted.internet import protocol,reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.tansport.getPeer().host
        print '...Connected from:',clnt

    def dataReceived(self,data):
        self.tansport.write('[%s] %s' % (ctime(),data))


factory = protocol.Factory()

factory.protocol = TSServProtocol

print 'Waiting fro connection...'


reactor.listenTCP(PORT,factory)
reactor.run()
