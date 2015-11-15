#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "weekend27"

# test urllib.request

from urllib import request
response = request.urlopen('http://www.zhihu.com/')
html = response.read()
print(html)
