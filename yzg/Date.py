#!/usr/bin/python
#-*- coding:utf-8 -*-

import time
import calendar

ticks = time.time()
print ticks

localtime = time.localtime(time.time())
print localtime

localtime1 = time.asctime(localtime)
print localtime1

print time.strftime("%Y %m %d, %H %M %S", localtime)

cal = calendar.month(2016, 1)
print cal

