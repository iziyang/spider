# -*- coding: utf-8 -*-
'''
for 循环实现的自动爬虫，基于 basic 模板
'''
import scrapy
from hellobi.items import HellobiItem
from scrapy.http import Request


class CourseSpider(scrapy.Spider):
    name = 'course'
    allowed_domains = ['hellobi.com']
    start_urls = ['https://edu.hellobi.com/course/1']

    def parse(self, response):
        item = HellobiItem()
        item['title'] = response.xpath('//ol/li[@class="active"]/text()').extract()
        item['link'] = response.xpath('//li[@class="active"]/a/@href').extract()
        item['amount'] = response.xpath('//span[@class="course-view"]/text()').extract()
        yield item
        for i in range(2, 256):
            url = 'https://edu.hellobi.com/course/' + str(i)
            yield Request(url, callback=self.parse)
