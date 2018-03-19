# -*- coding: utf-8 -*-
import pymysql.cursors

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        connection = pymysql.connect(host='127.0.0.1',
                                     user='root',
                                     passwd='root',
                                     db='dangdang',
                                     charset='utf8')
        cursor = connection.cursor()
        for i in range(0,len(item['title'])):
            titles = item['title'][i]
            sql = "INSERT INTO books(title) VALUES('"+titles+"')"
            cursor.execute(sql)
            connection.commit()
            print(titles)
        connection.close()
        return item
