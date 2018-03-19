# -*- coding: utf-8 -*-
"""
爬取当当网所有书籍信息，以 Python 为例，后续写进数据库
"""
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://www.dangdang.com/']

    def parse(self, response):
        item = DangdangItem()
        item['title']=response.xpath('//a[@class="pic"]/@title').extract()
        yield item
        for i in range(1,30):
            url = 'http://search.dangdang.com/?key=python&act=input&show=big&page_index='+str(i)
            yield Request(url,callback=self.parse)


