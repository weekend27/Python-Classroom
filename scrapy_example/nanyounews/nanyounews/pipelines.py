# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


# pipelines主要用于数据的进一步处理，比如类型转换、存储入数据库、写到本地等。
# pipelines是在每次spider中yield item 之后调用，用于处理每一个单独的item。

class NanyounewsPipeline(object):
    def __init__(self):
        self.file = open('nanyounews.txt', mode='wb')
    def process_item(self, item, spider):
        self.file.write(item['news_title'].encode("utf-8"))
        self.file.write("\n")
        self.file.write(item['news_date'].encode("utf-8"))
        self.file.write("\n")
        self.file.write(item['news_url'].encode("utf-8"))
        self.file.write("\n\n")
        # self.file.write("\n")
        return item
