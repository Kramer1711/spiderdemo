# -*- coding: utf-8 -*-
import scrapy
from oschina.items import OschinaItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['oschina.net']

    url = 'https://www.oschina.net/news/widgets/_news_index_generic_list?p=^index^&type=ajax'

    offset = 1

    start_urls = [url.replace('^index^', str(offset))]

    def parse(self, response):
        for each in response.xpath('//div[@class="content"]'):
            item = OschinaItem()

            item['title'] = zeroNodeInfo(each.xpath('./h3/a/text()').extract())
            item['paperUrl'] = zeroNodeInfo(each.xpath('./h3/a/@href').extract())
            item['desc'] = zeroNodeInfo(each.xpath('./div[@class="description"]/p/text()').extract())
            item['author'] = zeroNodeInfo(each.xpath('./div[@class="extra"]/div/div[1]/a/text()').extract())
            item['time'] = zeroNodeInfo(each.xpath('./div[@class="extra"]/div/div[2]/text()').extract())
            print(item)
            yield item

        if self.offset > 1:
            self.offset += 1

        yield scrapy.Request(self.url.replace('^index^', str(self.offset)), callback=self.parse)

    pass


def zeroNodeInfo(html):
    length = len(html)
    if length == 0:
        return ''
    elif length == 1:
        return html[0]
    else:
        return html
