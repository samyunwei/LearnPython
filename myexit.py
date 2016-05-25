# -*- coding: UTF-8 -*- 
# File Name: myexit.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年05月25日 星期三 22时18分05秒
#########################################################################
#!/usr/bin/env python
import sys

prev_exit_func = getattr(sys,'exitfunc',None)

def my_exit_func(old_exit = prev_exit_func):
    print 'Hello this is exit!'
    if old_exit is not None and callable(old_exit):
        old_exit()

sys.exitfunc = my_exit_func

