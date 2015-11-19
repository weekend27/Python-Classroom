#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2

response = urllib2.urlopen('http://www.zhihu.com')
print response.read()