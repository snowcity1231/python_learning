# -*- coding:utf8 -*-
# python列表可以是不同的数据类型
list = ['yes', 'no', 786, 3.14, 'tom', 70.2]
tinylist = [100, 'jack']

print('list = ', list)
print('list[0] = ', list[0])
print('list[1:3] = ', list[1:3])    #打印第二个到第三个元素
print('list[2:] = ', list[2:])      #打印第三个以后的元素
print('list[-1] : ', list[-1])      #打印最后一个元素
print('list[-3:-1]', list[-3:-1])   #打印倒数第三个到倒数第2个元素
print('tinylist * 2 : ', tinylist * 2)  #重复运算
print('list + tinylist : ', list + tinylist)    #表连接运算

