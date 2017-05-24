#!/usr/bin/python
#-*- coding:utf-8 -*-

dict1 = {}
dict1['one'] = "this is one"
dict1[2] = "this is two"

tinydict = {'name':'john', 'code':2332, 'dept':'sales'}
print dict1['one']
print dict1[2]
print tinydict
print tinydict.keys()
print tinydict.values()
print dict1.keys()

del dict1[2]

dict2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict2 = dict(a=1,b=2,c=3) #如果键都是字符串


#=================================方法
for k,v in dict2.iteritems(): #iteritems获得key，value的元组
    print k,v



#=================================技巧
dict3 = {x:x**2 for x in range(5)}
print dict3

