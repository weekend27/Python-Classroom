#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2
import cookielib

# 设置保存cookie的文件，同级目录下的cookie.txt
saveFile = 'cookie.txt'

# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(saveFile)

# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)

# 通过handler来构建opener
opener = urllib2.build_opener(handler)

# 创建一个请求，原理同urllib2的urlopen
response = opener.open('http://www.baidu.com')

# 保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)