#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib
import urllib2

// Wrong code!

url = "http://www.server.com/login"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username': 'weekend27', 'password': 'longlongpasswd'}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()