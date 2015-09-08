#########################################################################
#-*- coding:utf-8 -*-
# File Name: dmoz_spider.py
# Author: wayne
# mail: @163.com
# Created Time: 2015年09月08日 星期二 10时15分50秒
#########################################################################
#!/bin/python
import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["domz.org"]
    start_urls=[
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
            ]

    #def parse(self, response):
    #    filename = response.url.split("/")[-2]
    #    with open(filename, "wb") as f:
    #        f.write(response.body)

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            des = sel.xpath('text()').extract()
            print title 
            print "-"*30
            print link
            print "*"*30
            print des
            print "="*30