# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq


class NeteasespiderSpider(scrapy.Spider):
    name = 'neteaseSpider'
    allowed_domains = ['music.163.com/']
    # start_urls = ['https://music.163.com/#/discover/toplist?id=19723756/']
    start_urls = ['https://music.163.com/discover/toplist?id=19723756']
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Referer": "https://music.163.com/",
        "Upgrade-Insecure-Requests": '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'music.163.com',
        'Pragma': 'no-cache',
    }

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=self.headers)

    def parse(self, response):
        doc = pq(response.body.decode(response.encoding))#转成utf8编码并交给pyquery处理

        pass
