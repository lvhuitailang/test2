# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['tieba.com']
    url='https://tieba.baidu.com/f?kw=%E9%87%8D%E5%BA%86&ie=utf-8&pn='    # 基础URL地址
    start_urls =  ("http://tieba.baidu.com/f?kw=%D6%D8%C7%EC&fr=ala0&tpl=5",)   #具体贴吧地址  这一行必须这样子
    tiebaurl = 'https://tieba.baidu.com'   #贴吧地址


    def parse(self, response):
        sel=Selector(response)
        titles = sel.xpath('//ul[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a')
        for perTitle in titles:
            print(perTitle.xpath('string(.)').extract()[0])
