#!/usr/bin/python

#-*- coding:utf-8 -*-

dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"

tinydict = {'name':'john', 'code':2332, 'dept':'sales'}
print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()
print dict.keys()

del dict[2]

