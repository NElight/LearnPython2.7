#!/usr/bin/python
#-*- coding:utf-8 -*-

num = 0
while num < 9:
    print num
    num += 1
else:
    print "while can use else"
    
    
for letter in "python":
    print letter
    
for index in range(len("frult")):
    print "frult"[index]
    
for lette in "python":
    print letter
    
else:
    print "haha"
    
def sub():
    pass
for index in (1,3,4,5):
    if(index == 3):
        continue
    if(index == 4):
        break;
else:
    print "lala" 