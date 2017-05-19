#!/usr/bin/python
#-*- coding:utf-8 -*-

def printme(str):
    print str;
    return

printme("abc")

def changeInt(a):
    a = 10
    
b = 2
changeInt(b)
print b

def changeme(a):
    a.append([1,2,3,4])

c = [2, 3, 54]
changeme(c)
print c

def test1(name, age):
    print name,age;
    
test1("yzg", 24)
test1(age = 24, name = "yzg")

def printInfo(name, age = 14, *moreinfo, **moredic):
    print name, " ",
    print age, " ",
    for i in moreinfo:
        print i, " ",
    for (key, value) in moredic.items():
        print key, ":", "value",

printInfo("yzg", 24, 3, 4, 5, 32,7, host="shangjie",school="zzu")

#lambda
print
sum = lambda arg1, arg2 : arg1 + arg2
print sum(1, 2)

    