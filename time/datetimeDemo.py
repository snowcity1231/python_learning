# -*- coding: UTF-8 -*-

import datetime

i = datetime.datetime.now()
print "当前日期和时间是:", i
print "ISO格式时间:", i.isoformat()
print "当前年份:", i.year
print "当前月份：", i.month
print "当前日期：", i.day
print "当前小时:", i.hour
print "当前分钟：", i.minute
print "当前秒：", i.second
print "dd/mm/yyyy 格式时间: ",("%s/%s/%s" % (i.day, i.month, i.year))