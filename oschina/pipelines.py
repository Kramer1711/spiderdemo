# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from oschina.repository.conn import conn


class OschinaPipeline(object):
    connClass = None
    connect = None

    def __init__(self):
        self.connClass = conn()
        self.connect = self.connClass.getCon()
        self.filename = open("../oschina.json", "wb")

    def process_item(self, item, spider):
        # text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        # self.filename.write(text.encode('utf-8'))
        cursor = self.connect.cursor()
        cursor.execute('INSERT INTO oschina_spider(title,`desc`,url,author,time) VALUES (%s,%s,%s,%s,%s)',
                       [item['title'], item['desc'], item['paperUrl'], item['author'], item['time']])
        self.connect.commit()
        return item

    def close_spider(self, spider):
        self.connClass.close()
        self.filename.close()
