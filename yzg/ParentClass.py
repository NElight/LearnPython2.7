#!/usr/bin/python
#-*- coding:utf-8 -*-


class Parent:        # 定义父类
    parentAttr = 100
    _myname = "yzg" #protected
    __myage = 34 #private
    def __privatefunc(self):
       print "privatefunc"
       
    def _protectfunc(self):
       pass
       
    def __init__(self):
      print "调用父类构造函数"
 
    def parentMethod(self):
      print '调用父类方法'
 
    def setAttr(self, attr):
      Parent.parentAttr = attr
 
    def getAttr(self):
      print "父类属性 :", Parent.parentAttr
 
class Child(Parent): # 定义子类
    
    @classmethod
    def hi(cls, x):
        print cls._myname * x
        
    @staticmethod
    def add(a, b):
        print a + b
    
    
    def __init__(self):
        super(Child, self).__init__();
        print "调用子类构造方法"
 
    def childMethod(self):
        print '调用子类方法 child method'
 
c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法