#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2

request = urllib2.Request('http://www.weekend27.com/page')
try:
	urllib2.urlopen(request)
except urllib2.URLError, e:
	if hasattr(e, 'code'):
		print e.code
	if hasattr(e, 'reason'):
		print e.reason
else:
	print 'OK'