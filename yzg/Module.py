#!/usr/bin/python
#-*- coding:utf-8 -*-

import math
from _threading_local import local

def printHello(str):
    print "hello", str;

author = "yzg"


money = 2100;
def addMoney():
    global money
    money = money + 12222
    print money
addMoney()

content = dir(math)
print content

content1 = locals(math)
content2 = globals(math)
print content1, content2

#重新加载
reload(math)


    