# -*-coding:utf-8 -*-
# File Name: hotel.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
class HotelRoomClac(object):
    'Hotel room rate calculator'
    def __init__(self,rt,sales=0.085,rm=0.1):
        ''''HotelRoomClac default argument:
        sales tax == 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self,days=1):
        'Calculate total;default to daily rate'
        daily = round((self.roomRate * (1+self.roomTax + self.salesTax)),2)
        return float(days) * daily


sfo =HotelRoomClac(299)
print sfo.calcTotal()
print sfo.calcTotal(2)
sea = HotelRoomClac(189,0.086,0.058)
print sea.calcTotal(4)
