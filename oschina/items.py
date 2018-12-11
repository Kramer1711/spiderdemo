# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OschinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 链接地址
    paperUrl = scrapy.Field()
    # 摘要
    desc = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 发表时间
    time = scrapy.Field()
    pass
