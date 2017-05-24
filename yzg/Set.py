#!/usr/bin/python
#-*- coding:utf-8 -*-

list1 = [1, 3, 4, 5, 6 ,7 ,8 , 1]
set1 = set(list1);
print set

str_set = set('abcdefg')
print str_set



#================set技巧
set2 = {x for x in 'abcdefgaaa' if x not in 'ef'}
print set2