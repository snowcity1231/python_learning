# -*- coding: UTF-8 -*-

# 访问字符串中的值
var1 = 'Hello World'
var2 = 'Python'

print "var1[0]: ", var1[0]
print "var2[1:5]:", var2[1:5]

# 字符串连接
print "输出1: ", var1[:6] + var2

# 重复输出
print "输出2: ", var1[:6] * 2

# 是否包含字符串
print "输出3: ", "H" in var1
print "输出4: ", "M" not in var1

# 字符串转义r/R
print "输出5：", "a\nb"
print "输出6: ", r'a\nb'
print "输出7: ", R'a\nb'

# 字符串格式化
print "My name is %s and age is %d!" % ('Tom', 21)

# 三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
hi = '''hi
there'''
print hi