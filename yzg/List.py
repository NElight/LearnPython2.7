#!/usr/bin/python
#-*- coding:utf-8 -*-

list = ['runoob', 34, 23.23,'john',20.2]
tinylist = [123, 'john']

print list
print list[0]
print list[1:3]
print list[2:]
print list * 2
print list + tinylist

del list[2] #按照索引来删除列表中的元素
print list

#=====================列表方法
list.append(23) #用于添加元素
length = len(list)
list2 = range(0, 10, 3) #用于生成等差数列的数组，从0到10，以3为步长

list3 = filter(lambda a : a % 2 == 0, [1, 2, 3, 4, 5, 6])
print "==========", list3
list4 = map(lambda a: a * a, [1, 2, 3, 4, 5, 6])
print "=============", list4
list4 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6]) # reduce返回单值，先列表前两个元素作为参数调用函数，然后将结果和后面的元素一次作为参数调用函数
print "-----------", list4

for x in reversed(list3):
    print x
for x in sorted(list3):
    print x
                            




#====================列表技巧
for i in range(len(list)):
    print list[i]
    
list5 = [x * x for x in range(10)] #使用列表推导式
print list5
list6 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] #复杂的列表推导式，后面可以有多个for和if子句

#列表推导式的嵌套
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
list7 = [[row[i] for row in matrix] for i in range(4)] #行列转置
print list7








    
