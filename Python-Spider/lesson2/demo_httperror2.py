#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2

request = urllib2.Request('http://www.weekend27.com')
try:
	urllib2.urlopen(request)
except urllib2.HTTPError, e:
	print e.code
except urllib2.URLError, e:
	print e.reason
else:
	print 'OK'