# -*- coding: UTF-8 -*-

for letter in 'Python':
    print '当前字母：', letter

print

fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print '当前水果：', fruit

print
# 通过序列迭代索引
for index in range(len(fruits)):  # 内置函数len()返回列表长度，range()返回一个序列的数
    print '当前水果：', fruits[index]

print
# for...else else会在循环正常执行完(不通过break)的情况下执行
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print '%d 等于 %d * %d' % (num, i, j)
            break
    else:
        print num, '是一个质数'
