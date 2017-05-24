#!/usr/bin/python
#-*- coding:utf-8 -*-

import os

# str = raw_input("who are you\n")
# print str
a=1/7
print str(a)
print repr(a)

print range(2, 10, 2)

# str = input("input a line\n")
# print str

fo = open("foo.txt", "wb")
print fo.name
print fo.closed
print fo.mode
print fo.softspace

fo.write("this is a python fileIO")

fo = open("foo.txt", "r+")
str = fo.read(10)
print str

position = fo.tell()
print position

fo.seek(0, 0)
str = fo.read(10)
print str


fo.close()

# os.rename("foo1.txt", "foo.txt")
# os.remove("foo.txt")
# os.mkdir("testdir")
# os.chdir("../")
# os.getcwd()
# os.rmdir("testdir")


 

