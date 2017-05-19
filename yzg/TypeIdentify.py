#!/usr/bin/python
#-*- coding:utf-8 -*-
from __builtin__ import int
#type()不会认为子类是一种父类类型。
#isinstance()会认为子类是一种父类类型。
a = 1;
b = "my name";
print type(a)
print type(b)

print isinstance(a, int)
list = [1, 32, 34];
print a in list;
if (a not in list):
    print "hahah"

c = 1
if (a is c):
    print "a == c"
if (a is not c):
    print "a != c"