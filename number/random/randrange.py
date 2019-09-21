# -*- coding: UTF-8 -*-
# randrange() 方法返回指定递增基数集合中的一个随机数，基数默认值为1
import random

# random.randrange ([start,] stop [,step])
# start -- 指定范围内的开始值，包含在范围内。
# stop -- 指定范围内的结束值，不包含在范围内。
# step -- 指定递增基数

print "randrange(100, 1000, 2): ", random.randrange(100, 1000, 2)
print "randrange(0, 1000, 3): ", random.randrange(0, 1000, 3);