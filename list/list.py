# -*- coding: UTF-8 -*-
# 列表的数据项不需要具有相同的类型

list1 = ['physics', 'chemistry', 1997, 2000]

#列表截取
print "list1[0]: ", list1[0]
print "list1[2:5]: ", list1[1:3]
print "list1[-2]:", list1[-2]

# 扩展列表
list = []
list.append('Google')
print "list: ", list

# 删除元素
print 'list1:', list1
del list1[2]
print "after deleting list1:", list1

# 列表操作符
print "长度:", len(list1)
print "组合: ", list1 + list1
print "重复: ", list1 * 3
print "是否存在: ", 1998 in list1
print "迭代:",
for x in list1 : print x,",",
print