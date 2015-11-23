#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = "weekend27"

# fetch duanzi in one page

import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')

	'''
	pattern = re.compile(r'<div.*?author clearfix">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
	items = re.findall(pattern, content)
	# 发布人，发布时间，发布内容，附加图片以及点赞数: item[0] - item[4]
	for item in items:
		haveImg = re.search("img", item[3])
		if not haveImg:
			print item[0],item[1],item[2],item[4]
	'''


	pattern = re.compile(r'<div.*?class="author.*?>.*?<a.*?href.*?title="(.*?)">.*?</a>.*?<div.*?class="content">(.*?)<!--.*?</div>.*?<div.*?class="stats.*?<i.*?class="number">(.*?)</i>', re.S)
	items = re.findall(pattern, content)
	# print(items)
	for item in items:
		print 'author:', item[0]
		print 'content:',item[1]
		print 'like:',item[2]
		print '***********************************************************'
	

# catch error
except urllib2.URLError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason
