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
test1(age = 24, name = "yzg") #使用关键字进行赋值

def printInfo(name, age = 14, *moreinfo, **moredic):
    """Print the person info
        
    this is a document,
    func printInfo is the func that print the detail
    
    """
    
    print name, " ",
    print age, " ",
    for i in moreinfo:
        print i, " ",
    for (key, value) in moredic.items():
        print key, ":", "value",

printInfo("yzg", 24, 3, 4, 5, 32,7, host="shangjie",school="zzu")
print printInfo.__doc__

#lambda
print
sum = lambda arg1, arg2 : arg1 + arg2
print sum(1, 2)

#==============================注意事项
def test2(a, b=[]): #b默认的值只会赋值一次，所以如果改变了b的值，再次调用函数时，b的值已经更改,请使用test3方法来避免这种情况
    b.append(a)
    return b
print test2(1)
print test2(2)

def test3(a, b = None):
    if b == None:
        b = [];
    b.append(a)
    return b

    