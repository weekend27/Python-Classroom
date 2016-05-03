# -*- coding: utf-8 -*-

__author__ = "weekend27"

import scrapy
from nanyounews.items import NanyounewsItem
import logging

class nanyounewsSpider(scrapy.Spider):
    name = "nanyounewsSpider"
    allowed_domains = ["njupt.edu.cn"]
    start_urls = ["http://news.njupt.edu.cn/s/222/t/1100/p/1/c/6866/i/1/list.htm"]

    def parse(self, response):
        # 每页的新闻数量
        news_page_num = 14
        # 一共多少页
        page_num = 386
        if response.status == 200:
            for i in range(2, page_num+1):
                for j in range(1, news_page_num+1):
                    item = NanyounewsItem()
                    # 通过|连接xpath可以一次返回多个想要抓取的xpath
                    item['news_url'],item['news_title'],item['news_date'] = response.xpath(
                    "//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/font/text()"
                    "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//td[@class='postTime']/text()"
                    "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/@href").extract()
                    # 将url加上前缀
                    item['news_url'] = "http://news.njupt.edu.cn" + item['news_url']
                    # 将存储下来的item交给后续的pipelines处理
                    yield item

                # 通过生成next_page_url来通过scrapy.Request抓取下一页的新闻信息
                next_page_url = "http://news.njupt.edu.cn/s/222/t/1100/p/1/c/6866/i/"+str(i)+"/list.htm"
                # scrapy.Request的两个参数：一个是请求的URL，另外一个是回调函数用于处理这个request的response，这里我们的回调函数是parse_news
                yield scrapy.Request(next_page_url, callback = self.parse_news)

    def parse_news(self, response):
        news_page_num = 14
        if response.status == 200:
            for j in range(1,news_page_num+1):
                item = NanyounewsItem()
                item['news_url'],item['news_title'],item['news_date'] = response.xpath(
                "//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/font/text()"
                "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//td[@class='postTime']/text()"
                "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/@href").extract()
                yield item
