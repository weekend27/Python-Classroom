# -*- coding: utf-8 -*-

import scrapy
import requests
import os
from wangyuantu.items import WangyuantuItem

class WangyuantuSpider(scrapy.Spider):
    name = "wangyuantu"
    allowed_domains = ["tieba.baidu.com/p/3888309273"]
    start_urls = [
        'http://tieba.baidu.com/p/3888309273?pn=%d' % i for i in range(21,45)
        ]

    def parse(self, response):
        item = WangyuantuItem()
        item['image_urls']=response.xpath("//img[@class='BDE_Image']/@src").extract()

        yield item
