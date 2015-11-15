#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "weekend27"

# test urllib.request

import urllib.request

url = "http://www.zhihu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('utf-8')
print(data)
