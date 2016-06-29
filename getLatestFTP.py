# -*-coding:utf-8 -*-
# File Name: getLatestFTP.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
import ftplib
import os
import socket

HOST = '192.168.1.1'
DIRN = './'
FILE = 'testfile'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error,socket.gaierror),e:
        print 'ERROR:cannot reach "%s"' % HOST
        return

    try:
        f.login('username','password')
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'
        f.quit()
        return

    print '*** Logged in as "anonymouslyus"'


    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % DIRN
        f.quit()
        return
    print '*** Chaned to "%s" folder' % DIRN

    try:
        f.retrbinary('RETR %s' % FILE,open(FILE,'wb').write)
    except ftplib.error_perm:
        print 'ERROR : cannot read file "%s"' % FILE
        os.unlink(FILE)
    else:
        print '*** Downloadded "%s" to CWD'  % FILE
    f.quit()
    return

if __name__ == '__main__':
    main()
