#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib
import urllib2

values = {}
values['username'] = 'yourusername'
values['password'] = 'yourpassword'
data = urllib.urlencode(values)
url = 'http://passport.csdn.net/account/login'
geturl = url + '?' + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()