# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HellobiPipeline(object):
    def __init__(self):
        self.file = open('G:/python/Spider/DataAnalysis/scrapy/hellobi/hellobi/course.txt', 'a')

    def process_item(self, item, spider):
        print(item)
        print(item['title'])
        print(item['link'])
        print(item['amount'])
        print('------------')
        self.file.write(item['title'][0]+'\n'+item['link'][0]+'\n'+item['amount'][0]+'\n'+'---------')

    def close_spider(self):
        self.file.close()
