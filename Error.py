# -*- coding: UTF-8 -*- 
# File Name: Error.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年04月11日 星期一 19时59分30秒
#########################################################################
#!/usr/bin/env python
def Safe_float(obj):
    try:
        retval = float(obj)
        return retval
    except ValueError:
        retval = 'unvalid value!' 
        return retval

print Safe_float('foo')
print Safe_float('12.34')
