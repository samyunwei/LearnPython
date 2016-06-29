# -*-coding:utf-8 -*-
# File Name: uniFile.py
# Author: Sam
# mail: samyunwei@163.com
#########################################################################
#!/usr/bin/env python
FILE = 'unicode.txt'
CODEC = 'utf-8'
hello_out = u"Hello world\n"
bytes_out = hello_out.encode(CODEC)

f = open(FILE,"w")
f.write(bytes_out)
f.close()

f = open(FILE,"r")
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)

print hello_in

