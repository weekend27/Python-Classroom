#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2

request = urllib2.Request(uri, data=data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)