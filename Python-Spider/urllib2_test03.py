#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "weekend27"

# test urllib.request

import urllib
import urllib.request

data={}
data['word'] = '知乎日报'

url_values = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + url_values

data = urllib.request.urlopen(full_url).read()
data = data.decode('utf-8')
print(data)

