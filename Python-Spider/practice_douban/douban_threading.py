#! /usr/biin/env python2
# -*- coding:utf-8 -*-

__author__ = "weekend27"

# 一个简单的Python爬虫, 用于抓取豆瓣电影Top250的电影的名称
# 使用多线程

import urllib2
import re
import string
import threading
import Queue
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
_MOVIE = []
# FILE_LOCK = threading.Lock()
SHARE_Q = Queue.Queue()
_WORKER_THREAD_NUM = 3

class MyThread(threading.Thread):
	def __init__(self, func):
		super(MyThread, self).__init__()  # 调用父类的构造函数
		self.func = func   # 传入线程函数逻辑

	def run(self):
		self.func()

def worker():
	global SHARE_Q
	while not SHARE_Q.empty():
		url = SHARE_Q.get()   # 获得任务
		my_page = get_page(url)
		get_title(my_page)   # 获得当前页面的电影名
		time.sleep(1)
		SHARE_Q.task_done()

def get_page(url):
	'''
	根据当前页码爬取网页HTML
	Args: 
		cur_page: 表示当前所抓取的网站页码
	Returns:
		返回抓取到整个页面的HTML(unicode编码)
	Raises:
		URLError:url引发的异常
	'''
	try:
		my_page = urllib2.urlopen(url).read().decode("utf-8")
	except urllib2.URLError, e:
		if hasattr(e, 'code'):
			print 'The server could not fullfill the request.'
			print 'Error code: %s' % e.code
		elif hasattr(e, 'reason'):
			print 'We failed to reach a server. Please check your url and read the reason.'
			print 'reason: %s' % e.reason
	return my_page

def get_title(my_page):
	'''
	通过返回的整个网页HTML, 正则匹配前100的电影名称
	Args:
		my_page: 传入页面的HTML文本用于正则匹配
	'''
	temp_data = []
	pattern = re.compile('<span.*?class="title">(.*?)</span>', re.S)
	movie_items = re.findall(pattern, my_page)
	for index, item in enumerate(movie_items):
		if item.find('&nbsp') == -1:
			temp_data.append(item)
	_MOVIE.append(temp_data)

def main():
	global SHARE_Q
	threads = []
	douban_url = 'http://movie.douban.com/top250?start={page}&filter=&type='
	# 向队列中放入任务, 真正使用时, 应该设置为可持续的放入任务
	for index in xrange(10):
		SHARE_Q.put(douban_url.format(page = index * 25))
	for i in xrange(_WORKER_THREAD_NUM):
		thread = MyThread(worker)
		thread.start()
		threads.append(thread)
	for thread in threads:
		thread.join()
	SHARE_Q.join()
	with open('douban_movie.txt', 'w+') as my_file:
		for page in _MOVIE:
			for movie_name in page:
				my_file.write(movie_name + '\n')
	print 'Douban Spider Successful!!!'

if __name__ == '__main__':
	main()