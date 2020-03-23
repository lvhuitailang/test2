# -*- coding: utf-8 -*-
import scrapy

from pyquery import PyQuery as pq
from cartoonSpider.cSpider.items import Chapter
from cartoonSpider.cSpider.items import ChapterDetail
import execjs
from cartoonSpider.cSpider.utils.base64Decode import base64Decode
import re

class AlimanhuaSpider(scrapy.Spider):
    name = 'alimanhua'
    allowed_domains = ['www.alimanhua.com']
    start_urls = ['http://www.alimanhua.com/manhua/419/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
    }
    #js 解码页码
    ctx = execjs.compile(base64Decode)


    def parse(self, response):
        doc = pq(response.body.decode(response.encoding))#转成utf8编码并交给pyquery处理
        title = doc('.titleInfo h1').text()
        lst = []
        liList = doc('#section ul li')
        for li in liList.items():
            c = li('a')
            chapter = Chapter()
            chapter['title'] = title
            chapter['type'] = 1
            chapter['chapterTitle'] = c.attr('title')
            chapter['chapterUrl'] = self.allowed_domains[0] + c.attr('href')
            lst.append(chapter)
            yield chapter
            yield scrapy.Request('http://'+chapter['chapterUrl'], meta={'chapter':chapter},callback=self.parse_detail,dont_filter=True,headers=self.headers)


    #这一张的总页数
    def parse_detail(self,response):
        chapter = response.meta['chapter']
        doc = pq(response.body.decode(response.encoding))#转成utf8编码并交给pyquery处理

        #总页数的base64正则选取
        searchObj = re.search( r'packed="(.*)"', doc.text(), re.M|re.I)
        base64CodeString = ''
        if searchObj is not None:
            base64CodeString = searchObj.group(1)
        else:
            print('error')
            return None

        #解码总页数（根据网站的规则）
        pageList = self.ctx.call('getResult',base64CodeString)
        pageCount = len(pageList) - 1 #这一张的总页数
        for pageIndex in range(pageCount):
            yield scrapy.Request('http://'+chapter['chapterUrl']+'?page='+str(pageIndex+1), meta={'chapter':chapter,'currPage':pageIndex+1,'pageList':pageList},callback=self.parse_detail_every_page,dont_filter=True,headers=self.headers)



    #爬取每一页的漫画
    def parse_detail_every_page(self,response):
        chapter = response.meta['chapter']
        currPage = response.meta['currPage']#当前页
        pageList = response.meta['pageList']#页码列表
        doc = pq(response.body.decode(response.encoding))#转成utf8编码并交给pyquery处理

        searchObj = re.search( r'\/(\d+)?\.', chapter['chapterUrl'], re.M|re.I)
        chapterId = searchObj.group(1)


        chapterDetail = ChapterDetail()

        chapterDetail['title'] = chapter['title']
        chapterDetail['type'] = 2
        chapterDetail['chapterId'] = chapterId
        chapterDetail['chapterTitle'] = chapter['chapterTitle']
        chapterDetail['chapterUrl'] = chapter['chapterUrl']
        chapterDetail['page'] = currPage
        chapterDetail['pageUrl'] = chapter['chapterUrl']+'&page='+str(currPage)

        imgserver = r'http://res.img.fffimage.com/'

        imageUrl = imgserver+pageList[currPage]
        chapterDetail['imageUrl'] = imageUrl



        yield chapterDetail



