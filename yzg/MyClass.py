#!/usr/bin/python
#-*- coding:utf-8 -*-

class Employee:
    empcount = 0
    def __init__(self,name,salary):
        self.name = name;
        self.salary = salary
        Employee.empcount += 1

    def desplaycount(self):
        print "total count %d" % Employee.empcount
        
    def desplayemployee(self):
        print "name", self.name, "salary:", self.salary
    
    def __del__(self):
        print "this object will be deinit"

a = Employee("yzg", 100000)
a.desplayemployee()
a.desplaycount()

a.age = 15
print a.age

del a.age
# print a.age

hasattr(a, "age")
getattr(a, "age")
setattr(a, "age", 123)
delattr(a, "age")



