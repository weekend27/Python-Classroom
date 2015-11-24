#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = "weekend27"

import urllib
import urllib2
import re

# 百度贴吧爬虫类
class BDTB:
	# 初始化，传入基地址，是否只看楼主的参数
	def __init__(self, baseUrl, seeLZ):
		self.baseUrl = baseUrl
		self.seeLZ = '?see_lz=' + str(seeLZ)

	# 传入页码，获取该页帖子的代码
	def getPage(self, pageNum):
		try:
			url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
			req = urllib2.Request(url)
			response = urllib2.urlopen(req)
			print response.read()
			return response
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print u"连接百度贴吧失败,错误原因:", e.reason
				return None

	def getTitle(self):
		page = self.getPage(1)
		pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)  # re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。
		result = re.search(pattern, page)
		if result:
			#print result.group(1)   # test output
			return result.group(1).strip()
		else:
			return None

	def getPageNum(self):
		page = self.getPage(1)
		pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
		result = re.search(pattern, page)
		if result:
			#print result.group(1)  # test output
			return result.group(1).strip()
		else:
			return None

	def getContent(self, page):
		pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
		items = re.findall(pattern, page)
		for item in items:
			print item


baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL, 1)
# bdtb.getPage(1)
# bdtb.getTitle()
bdtb.getContent(bdtb.getPage(1))
