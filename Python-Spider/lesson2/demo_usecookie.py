#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2
import cookielib

# 创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()

# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)

# 创建请求的request
req = urllib2.Request('http://www.baidu.com')

# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)

# 通过handler来构建opener
opener = urllib2.build_opener(handler)

response = opener.open(req)
print response.read()