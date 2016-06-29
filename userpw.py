# -*-coding:utf-8 -*-
# File Name: userpw.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
import time
db = {}

def newuser():
    prompt = 'login desired:'
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken,try another:'
            continue
        else:
            break
    pwd = raw_input('passwd:')
    l = []
    l.append(pwd)
    l.append(time.time())
    db[name] = l

def olduser():
    name = raw_input('login:')
    pwd = raw_input('passwd:')
    l = db.get(name)
    if len(l) > 0:
        passwd = l[0]
        logtime = l[1]
        print time.gmtime(logtime)
    if passwd == pwd:
        print 'welcome back',name
        l[1] = time.time()
    else:
        print 'login incorrect'
def deluser():
    name = raw_input('theuser:')
    if db.pop(name,None) != None:
        print 'rmove %s success' % name
    else:
        print 'user:%s not exist!' % name

def showall():
    for eachuser in db:
        print 'username:%s passwd:%s' % (eachuser,db[eachuser][0])
def showmenu():
    prompt = """
    (N)ew User login
    (E)xisting User login
    (Q)uit
    (D)elete user
    (S)how all user 
    Enter your choice """
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except(EOFError,KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked:[%s]' % choice
            if choice not in 'neqsd':
                print 'invalid option,try again'
            else:
                chosen = True
        if choice == 'q':
            done =True
        elif choice == 'n':
            newuser()
        elif choice == 'e':
            olduser()
        elif choice == 's':
            showall()
        elif choice == 'd':
            deluser()

if __name__ == '__main__':
    showmenu()

