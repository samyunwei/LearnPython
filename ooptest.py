# -*- coding: UTF-8 -*- 
# File Name: ooptest.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年05月09日 星期一 23时47分14秒
#########################################################################
#!/usr/bin/env python
class RoundFloatManual(object):
    def __init__(self,val):
        assert isinstance(val,float),'Values must be a float'
        self.value = round(val,2)

    def __str__(self):
        return '%.2f' % self.value

    __repr__ = __str__


rmp =  RoundFloatManual(3.2)
print rmp    
