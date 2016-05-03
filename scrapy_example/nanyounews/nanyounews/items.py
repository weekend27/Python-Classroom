# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NanyounewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    news_title = scrapy.Field()     # 南邮新闻标题
    news_date = scrapy.Field()      # 南邮新闻时间
    news_url = scrapy.Field()       # 南邮新闻详细链接
