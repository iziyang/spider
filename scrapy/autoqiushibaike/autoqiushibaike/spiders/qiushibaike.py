# -*- coding: utf-8 -*-
'''
基于模板 crawl 生成的自动爬虫
'''
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from  autoqiushibaike.items import AutoqiushibaikeItem


class QiushibaikeSpider(CrawlSpider):
    name = 'qiushibaike'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['http://www.qiushibaike.com/']

    def start_requests(self):
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        yield Request('http://www.qiushibaike.com', headers=header)

    rules = (
        Rule(LinkExtractor(allow=r'article'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = AutoqiushibaikeItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['content'] = response.xpath('//div[@class="content"]/text()').extract()
        i['link'] = response.xpath('//link[@rel="canonical"]/@href').extract()
        return i
