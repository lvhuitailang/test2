# -*- coding: utf-8 -*-
import scrapy

from pyquery import PyQuery as pq
from cSpider.items import CartoonChapter


class AlimanhuaSpider(scrapy.Spider):
    name = 'alimanhua'
    allowed_domains = ['www.alimanhua.com']
    start_urls = ['http://www.alimanhua.com/manhua/419/index.html']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
    }

    def parse(self, response):
        doc = pq(response.body.decode(response.encoding))#转成utf8编码并交给pyquery处理
        title = doc('.titleInfo h1').text()
        lst = []
        liList = doc('#section ul li')
        for li in liList.items():
            c = li('a')
            chapter = CartoonChapter()
            chapter['title'] = title
            chapter['chapterTitle'] = c.attr('title')
            chapter['chapterUrl'] = self.allowed_domains[0] + c.attr('href')
            lst.append(chapter)
            yield chapter
            yield scrapy.Request('http://'+chapter['chapterUrl'], callback=self.parse_detail,dont_filter=True,headers=self.headers)


    def parse_detail(self,response):
        doc = pq(response.body.decode(response.encoding))#转成utf8编码并交给pyquery处理
        aa = doc('.picNav #selectpage2')
        bbb = aa('option')
        ccc = bbb.end()
        totalPage = int(doc('#selectpage2 option:last-child').attr('value'))
        pass

