# -*- coding: utf-8 -*-
import scrapy
import json
import time
from pyquery import PyQuery as pq
from tiebaSpider.items import TieBaList

class MyspiderSpider(scrapy.Spider):
    #基础url
    staticUrl = 'https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn=0'
    #当前页
    currentPage = 0

    name = 'mySpider'
    allowed_domains = ['https://tieba.baidu.com']
    start_urls = [staticUrl]
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
    # }
    #
    # def start_requests(self):
    #     return [scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=self.headers)]
    #

    def parse(self, response):
        doc = pq(response.body.decode(response.encoding))#转成utf8编码并交给pyquery处理
        # text = response.body.decode(response.encoding)
        content = doc("#content_leftList")
        nextUrl = content('#frs_list_pager a.next').attr('href')


        # topicList = content('#thread_list')
        # self.parseList(topicList)
        if nextUrl is not None or nextUrl.length < 1:
            yield scrapy.Request('https:'+nextUrl, callback=self.parse,dont_filter=True)
        try:
            yield scrapy.Request(response.url, callback=self.parseList,dont_filter=True)
        except Exception as e :
            print('====================================================================')
            print(nextUrl)


    def parseList(self,response):
        aa = response.text
        doc = pq(response.body)#转成pyquery处理
        content = doc("#content_leftList")
        pqList = content('#thread_list')

        list = pqList('li.j_thread_list[data-field]').items()
        for floor in list:
            data_field = json.loads(floor.attr('data-field'))
            try:
                tId = floor.attr('data-tid')
                reply = data_field['reply_num'] if data_field['reply_num'] else 0
                author = data_field['author_name']
                title = floor('.t_con .threadlist_lz a.j_th_tit').attr('title')
                info = floor('.t_con .threadlist_lz a.j_th_tit').text()

                authorIdJson = json.loads(floor('.t_con .threadlist_author .tb_icon_author').attr('data-field'))
                authorId = authorIdJson['user_id']

                lastReplyContent = floor('.t_con .threadlist_detail .threadlist_abs').text()
                lastReplyName = floor('.t_con .threadlist_detail a.frs-author-name').text()
                lastReplyTime = floor('.t_con .threadlist_detail   .threadlist_author  span.threadlist_reply_date').eq(0).text()

                tieBa = TieBaList()
                tieBa['tId'] = str(tId)
                tieBa['reply'] = str(reply)
                tieBa['title'] = title
                tieBa['info'] = info
                tieBa['author'] = author
                tieBa['authorId'] = str(authorId)
                tieBa['lastReplyName'] = lastReplyName
                tieBa['lastReplyContent'] = lastReplyContent
                tieBa['lastReplyTime'] = lastReplyTime
                tieBa['tieUrl'] = r'https://tieba.baidu.com/p/'+str(tId)
                yield tieBa

            except Exception as e:
                print(e)
                continue





