#!/usr/bin/python
#-*- coding:utf-8 -*-
from symbol import argument

try:
    fh = open("test.txt", "w")
    try:
        fh.write("this is a test for exception")
    finally:
        fh.close()    
    
except IOError, argument:
    print "error: no file or open file error"
    print "errorcode:", argument
else:
    print "success"
    fh.close()
    
try:
    print 
except:
    print "error"
else:
    print "success"
    
try:
    print
finally:
    print "wo must close fileIO anytime"
    
def funcname(level):
    if(level > 1):
        raise Exception("invalid exception", level)
try:
    print 
except "invalid exception":
    print "this error occur"

class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.arg = arg
try:
    print 
except NetworkError:
    print "this is user error"

