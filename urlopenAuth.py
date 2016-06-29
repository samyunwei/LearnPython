# -*-coding:utf-8 -*-
# File Name: urlopenAuth.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
import urllib2

LOGIN = 'wesc'
PASSWD = "you 'llNeverGuess"
URL = 'http://localhost'

def handler_version(url):
    from urlparse import urlparse as up
    tempmgr = urllib2.HTTPPasswordMgr()
    tempmgr.add_password('Archives',up(url)[1],LOGIN,PASSWD)
    hdlr = urllib2.HTTPBasicAuthHandler(tempmgr)
    opener = urllib2.build_opener(hdlr)
    urllib2.install_opener(opener)
    return url



def request_version(url):
    from base64 import encodestring
    req = urllib2.Request(url)
    b64str = encodestring('%s:%s' % (LOGIN,PASSWD))[:-1]
    req.add_header("Authorization","Basic %s" % b64str)
    return req


for funcType in ('handler','request'):
    print '**** Using %s:' % funcType
    url = eval('%s_version' % funcType)(URL)
    f = urllib2.urlopen(url)
    print f.readline()
    f.close()


    

