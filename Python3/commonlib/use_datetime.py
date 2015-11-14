#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "weekend27"

# use datetime

from datetime import datetime, timedelta, timezone

# 获取当前datetime
now = datetime.now()
print('now =', now)
print('type(now) =', type(now))
print('**********************************************')

# 用指定日期时间创建datetime
dt = datetime(2099, 10, 24, 11, 11, 11) # 年月日时分秒
print('future time =', dt)
print('**********************************************')

# 把datetime转换成timestamp
print('datetime -> timestamp:', dt.timestamp())
print('**********************************************')

# 把timestamp转换成datetime
t = dt.timestamp()
print('timestamp -> datetime:', datetime.fromtimestamp(t)) # 本地时间
print('timestamp -> datetime as UTC+0:',datetime.utcfromtimestamp(t)) # UTC时间
print('**********************************************')

# 从str中读取datetime
oldday = datetime.strptime('2014-10-24 11:12:34', '%Y-%m-%d %H:%M:%S')
print('strptime:', oldday)
print('**********************************************')

# 把datetime格式化输出
print('strftime:', oldday.strftime('%a, %b %d %H:%M'))
print('**********************************************')

# 对日期进行加减
print('old datetime =', oldday)
print('old datetime + 10 hours =', oldday + timedelta(hours=10))
print('old datetime - 2 days =', oldday -timedelta(days=2))
print('old datetime + 2.5 days =', oldday + timedelta(days=2, hours=12))
print('**********************************************')

# 把时间从UTC+0时区转换为UTC+8
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt)
print('UTC+8:00 now =', utc8_dt)
print('**********************************************')
      
