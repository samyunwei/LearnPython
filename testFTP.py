# -*-coding:utf-8 -*-
# File Name: testFTP.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
from ftplib import FTP

f = FTP('192.168.1.1')

f.login('username','password')
print f.pwd()
print f.dir('./')
f.quit()

