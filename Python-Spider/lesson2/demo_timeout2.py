#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib
import urllib2

values = {'username':'10086@qq.com', 'password':'wojiubugaosunizenmezhao'}
data = urllib.urlencode(values)
response = urllib2.urlopen('http://www.zhihu.com', data, 10)
print response.read()