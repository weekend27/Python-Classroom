#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = "weekend27"


import scrapy
from tutorial.items import DmozItem

'''
创建一个Spider，必须继承 scrapy.Spider 类， 且定义以下三个属性:
(1) name: 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字。
(2) start_urls: 包含了Spider在启动时进行爬取的url列表。 因此，第一个被获取到的页面将是其中之一。
    后续的URL则从初始的URL获取到的数据中提取。
(3) parse() 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。
    该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。
'''
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    # 初期代码
    # def parse(self, response):
    #     filename = response.url.split("/")[-2]
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item

'''
具体过程：
Scrapy为Spider的 start_urls 属性中的每个URL创建了 scrapy.Request 对象，并将 parse 方法作为回调函数(callback)赋值给了Request。
Request对象经过调度，执行生成 scrapy.http.Response 对象并送回给spider parse() 方法。
'''
