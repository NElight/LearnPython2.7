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
    
    
#========================循环技巧
for i,v in enumerate([1,2,3,4,5]):
    print i, v
    
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions, answers): #使用zip将多个序列压在一起同时便利
    print q,a