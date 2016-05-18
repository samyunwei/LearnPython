# -*- coding: UTF-8 -*- 
# File Name: mydb.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年05月18日 星期三 20时34分29秒
#########################################################################
#!/usr/bin/env python
import os
import pickle
import time
import copy
class MyUserDB(object):
    def __init__(self,theUserName,thePassWord):
        self.userdbpath = './MyUserDB/'+ theUserName
        self.username = ''
        self.password = ''
        self.createtime = None
        self.lastlogtime = None
        self.initflag = False
        self.data = None
        if os.path.exists(self.userdbpath):
            try:
                with open(self.userdbpath,'r') as f:
                    tempuser = pickle.load(f)
                    if tempuser.password != thePassWord:
                        self.initflag = False
                        raise ValueError('password wrong!')
                    else:
                        tempuservars = vars(tempuser)
                        for eachattr in tempuservars.keys():
                            setattr(self,eachattr,tempuservars[eachattr])
                        self.initflag = True
            except IOError,e:
                print e
        else:
            self.username = theUserName
            self.password = thePassWord
            self.createtime = time.time()
            self.lastlogtime = self.createtime
            self.initflag = True
            print 'Create new User'
    
    def GetData(self):
        return self.data 

    def SetData(self,thedata):
        self.data = thedata 

    def __del__(self):
        if self.initflag:
            try:
                with open(self.userdbpath,'w') as f:
                    try:
                        pickle.dump(self,f)
                        pass
                    except pickle.PicklingError,e:
                        print e
            except IOError, e:
                print e
        else:
            pass

if __name__ == '__main__':
    test = MyUserDB('admin','admin')
    print test.createtime
    print test.username
    print test.lastlogtime
    print test.data
    test.SetData('Hello World33')
    del test
