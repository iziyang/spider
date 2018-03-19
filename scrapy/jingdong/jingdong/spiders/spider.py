# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jingdong.items import JingdongItem
import urllib.request
import re


class SpiderSpider(CrawlSpider):
    name = 'spider'
    allowed_domains = ['jd.com']
    start_urls = ['http://www.jd.com/']

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        try:
            i = JingdongItem()
            thisurl = response.url
            pat = 'https://item.jd.com/(.*?).html'
            x = re.search(pat, thisurl)
            if x:
                thisid = re.compile(pat).findall(thisurl)[0]
                print(thisid)
                title = response.xpath('//div[@class="p-name"]/a/text()').extract()
                link = response.xpath('//div[@class="p-name"]/a/@href').extract()
                priceurl = 'https://p.3.cn/prices/mgets?callback=jQuery6736606&type=1&area=1_72_4137_0&pdtk=&pduid=810691037&pdpin=&pin=null&pdbp=0&skuIds=J_'+str(thisid)+'&ext=11000000&source=item-pc'
                commenturl = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv69098&productId='+str(thisid)+'&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
                priceweb = urllib.request.urlopen(priceurl).read().decode('utf-8','ignore')
                commentweb = urllib.request.urlopen(commenturl).read().decode('utf-8','ignore')
                pricepat = '"p":"(.*?)"'
                commentpat = '"goodRateShow":(.*?),"'
                price = re.compile(pricepat).findall(priceweb)
                comment = re.compile(commentpat).findall(commentweb)
                if len(title) and len(link) and len(price) and len(comment):
                    print(title,link,price,comment)
                else:
                    pass
            else:
                pass
            return i
        except Exception as e:
            print(e)






