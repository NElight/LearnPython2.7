#!/usr/bin/python
#-*- coding:utf-8 -*-

tuple = ("runoob", 34, 2.34, "json",23.3)
tinytuple = (123, "johon")

print tuple
print tuple[0]
print tuple[1:3]
print tuple[:3]
print tuple[2:]
print tuple * 2
print tuple + tinytuple
#元组中的值不能改变
# tuple[2] = 23

del tinytuple
