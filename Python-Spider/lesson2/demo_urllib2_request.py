#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2

// suggest to write in this way, use request

request = urllib2.Request('http://www.zhibo8.cc')
response = urllib2.urlopen(request)
print response.read()