# -*-coding:utf-8 -*-
# File Name: ooptest.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
def AddrBookEntry(object):
    'address book enrty class'
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = ph
        print 'Created instance for:',self.name

    def updatePhone(self,newph):
        self.phone = newph
        print 'updatePhone# for :',self.name

class MyClass(object):
    'MyClass class definition'
    myVersion = '1.1'
    def showMyVersion(self):
        print MyClass.myVersion



print dir(MyClass)
print MyClass.__class__
