# -*- coding: UTF-8 -*- 
# File Name: MoneyFmt.py
# Author: Sam
# mail: samyunwei@163.com
# Created Time: 2016年05月16日 星期一 00时22分17秒
#########################################################################
#!/usr/bin/env python
class MoneyFmt(object):
    def __init__(self,theMoney):
        if isinstance(theMoney,float):
            self.moneynumber = theMoney
        else:
            raise TypeError('Init with Float')

    def dollarize(self):
        if self.moneynumber >= 0:
            return '$' + self.threenumbercut(str(self.moneynumber))
        else:
            return '-$' + self.threenumbercut(str(abs(self.moneynumber)))


    def threenumbercut(self,thenumstr,theprecise = 2):
        if isinstance(thenumstr,str):
            thenumstr = thenumstr.split('.')
            theint = thenumstr[0]
            lenint = len(theint)
            theResult = ""
            for i in range(lenint):
                if not ((i+1) % 3) and (i < lenint-1) :
                    theResult += theint[i]+','
                else:
                    theResult += theint[i]
            if len(thenumstr) > 1:
                thedecimal = thenumstr[1]
                thedecimal.ljust(theprecise)
                thedecimal.replace(' ','0')
                thedecimal = thedecimal[:theprecise]
                theResult += '.' + thedecimal
            else:
                theResult += '.' + theprecise*'0'
            return theResult
        else:
            raise TypeError



if __name__ == '__main__':
        testmoney = MoneyFmt(-122222223.72331)
        print testmoney.dollarize()
        
