#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib
import urllib2

// Not OK

values = {'username':'10086@qq.com', 'password':'wojiubugaosunizenmezhao'}
data = urllib.urlencode(values)
url = 'http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()