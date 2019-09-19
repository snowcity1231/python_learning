#!/usr/bin/python
# -*- coding: UTF-8 -*-

# python元组，只读，不能二次赋值

tuple = ('runoob', 786, 2.23, 'join', 70.2)
tinyTuple = (123, 'john')

print tuple  # 输出完整数组
print tuple[0]
print tuple[1:3]  # 输出第二至第四个(不包含)元素
print tuple[2:]  # 输出第三个至末尾的元素
print tinyTuple * 2  # 输出两次
print tuple + tinyTuple  # 组合数组