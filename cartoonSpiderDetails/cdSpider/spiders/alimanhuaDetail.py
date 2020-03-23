# -*- coding: utf-8 -*-
import scrapy
from cdSpider.utils.db  import DbPool

class AlimanhuadetailSpider(scrapy.Spider):
    name = 'alimanhuaDetail'
    allowed_domains = ['www.alimanhua.com']
    start_urls = ['http://www.alimanhua.com/']

    def parse(self, response):
        pass
