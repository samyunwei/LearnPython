# -*-coding:utf-8 -*-
# File Name: stack.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
stack = []
def pushit():
    stack.append(raw_input('Enter New string:').strip())

def popit():
    if len(stack) == 0:
        print 'Cannot pop from an empty stack!'
    else:
        print 'Removed [',`stack.pop()`,']'
def viewstack():
    print stack

CMDs = {'u':pushit,'o':popit,'v':viewstack}

def showmenu():
    pr = """
    p(U)sh
    po(O)P
    (V)iew
    (Q)uit

    Enter Choice:"""
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice = 'q'
            print '\nYou Picked:[%s]' % choice
            if choice not in 'uovq':
                print 'Invalid option,try again'
            else:
                break
        if choice == 'q':
            break
        CMDs[choice]()
if __name__ == '__main__':
    showmenu()
