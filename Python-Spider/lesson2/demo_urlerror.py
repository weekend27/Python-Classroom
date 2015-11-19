#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2

request = urllib2.Request('http://www.asdfaouqwernnlao.com')
try:
	urllib2.urlopen(request)
except urllib2.URLError, e:
	print e.reason