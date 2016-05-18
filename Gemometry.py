# -*- coding: UTF-8 -*- 
# File Name: Gemometry.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年05月19日 星期四 00时01分44秒
#########################################################################
#!/usr/bin/env python
import os
import copy
import math
class Point(object):
    def __init__(self,thex = 0,they = 0):
        if (isinstance(thex,float) or isinstance(thex,int)) and (isinstance(they,float) or isinstance(they,int)):
            self.x = thex
            self.y = they
        else:
            raise TypeError('X,Y must float or int') 


class Line(object):
    'Line Object'
    def __init__(self,P1,P2):
        if isinstance(P1,Point) and isinstance(P2,Point):
            self.P1 = copy.deepcopy(P1)
            self.P2 = copy.deepcopy(P2)
        else:
            raise TypeError('P1,P2 must be class of Ponit')

    def length(self):
        return math.sqrt((self.P1.x - self.P2.x)**2 + (self.P1.y - self.P2.y)**2)

    def slope(self):
        theslope = 0
        try:
            theslope = (self.P1.y - self.P2.y) / (self.P1.x - self.P2.x)  
        except ZeroDivisionError:
            theslope = None
        finally:
            return theslope

    def __repr__(self):
        return ((self.P1.x,self.P1.y),(self.P2.x,self.P2.y))

    def __str__(self):
        return str(self.__repr__())

if __name__ == '__main__':
    p1 = Point(1.22,2)
    p2 = Point(2,3.3)

    l = Line(p1,p2)
    print l.length()
    print l.slope()
    print l
    
