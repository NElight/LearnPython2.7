#!/usr/bin/python
#-*-coding:utf-8-*-

s = 'ilovepython';
print s;
print s[1:5];
print s[0];
print s[2:5];
print s[2:];
print s * 2;  # *号操作符重复字符串
print s + "test"; # +号操作符连接两个字符串
str = "a" "b" #相邻的两个字符串会自动的连接在一起

print str


print "hahah\n"
print r"hahah\n" #字符串前面加r不转义

name = "yzg";
age = 26
print "name: %s age: %d " % (name, age)

str = """\   #如果第一行有反斜线，此行不显示
asf das dfasf d
as fasdf af sa
asf dsadf 
"""
print str

#==========================字符串函数
length = len(str)  #计算字符串长度
print length




