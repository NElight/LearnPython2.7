#!/usr/bin/python
#-*- coding:utf-8 -*-

list = ['runoob', 34, 23.23,'john',20.2]
tinylist = [123, 'john']

print list
print list[0]
print list[1:3]
print list[2:]
print list * 2
print list + tinylist

del list[2]
print list