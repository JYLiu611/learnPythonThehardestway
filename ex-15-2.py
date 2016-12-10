#-*- coding:utf-8 -*-
from sys import argv
script,name1,name2=argv
x=open(name1).read()
open(name2,'w').write(x)
#

