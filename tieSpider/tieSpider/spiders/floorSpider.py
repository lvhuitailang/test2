# -*- coding: utf-8 -*-
import scrapy
import json
import time
import re
import pymysql
from pyquery import PyQuery as pq

from tieSpider.items import TieItem

class FloorspiderSpider(scrapy.Spider):
    name = 'floorSpider'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/p/6197240266']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
    }

    def __init__(self, db_parmars):
        self.db_parmars = db_parmars

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        '''
        初始化数据库
        :param crawler:
        :param args:
        :param kwargs:
        :return:
        '''
        db_parmars = {
            'host': crawler.settings['MYSQL_HOST'],
            'database': crawler.settings['MYSQL_DB'],
            'port': crawler.settings['MYSQL_PORT'],
            'user': crawler.settings['MYSQL_USER'],
            'password': crawler.settings['MYSQL_PASSWORD'],
            'charset': crawler.settings['MYSQL_CHARSET'],
        }
        spider = cls(db_parmars,*args,**kwargs)
        return spider

    def start_requests(self):
        '''
        从数据库里面取出所有帖子的url
        :return:
        '''
        if self.db_parmars is not None:
            conn = pymysql.Connect(**self.db_parmars)
            cursor = conn.cursor()
            sql = r'select tieUrl from tielist'
            lines = cursor.execute(sql)
            urlList = tuple()
            if lines is not None and lines > 0:
                urlList = cursor.fetchall()
            cursor.close()
            conn.close()

            for urlItem in urlList:
                yield scrapy.Request(urlItem[0], callback=self.parse,dont_filter=True)





    def parse(self, response):
        doc = pq(response.body.decode(response.encoding))#转成utf8编码并交给pyquery处理
        nextLabel = doc('#container .pb_footer .p_thread .pb_list_pager a:contains("下一页")')

        if nextLabel is not None and nextLabel.length > 0:
            nextUrl = 'https://tieba.baidu.com'+nextLabel.attr('href')#下一页url
            yield scrapy.Request(nextUrl, callback=self.parse,dont_filter=True)
        try:
            yield scrapy.Request(response.url, callback=self.parse_Content,dont_filter=True,headers=self.headers)
        except Exception as e :
            print('====================================================================')
            print(nextUrl)

    def parse_Content(self,response):
        doc = pq(response.body.decode(response.encoding))#转成utf8编码并交给pyquery处理
        try:
            title = doc('#container .pb_content #j_core_title_wrap .core_title_txt').attr('title').strip() #帖子标题
        except Exception as e:
            print(e)
            return None

        reg = re.compile(r'(\d+)\?*')
        tId = re.search(reg,response.url).group(0)  #用正则从url里面提取帖子id
        tieUrl = response.url   #帖子链接

        floorList = doc('#container .p_postlist .j_l_post[data-field]')#所有楼层列表
        for floorItem in floorList.items():
            data_field = json.loads(floorItem.attr('data-field'))
            if data_field is None:
                continue

            isOwner = '1' if floorItem('.d_author .louzhubiaoshi').length > 0 else '0'  #是否是楼主
            userHeadUrl = floorItem('.d_author .p_author .icon img').attr('src')    #层主头像链接
            userId = data_field['author']['user_id']    #层主id
            username = data_field['author']['user_name']    #层主名字

            pId = data_field['content']['post_id']    #楼层id（回复id，每一条回复的唯一标识）
            floor = data_field['content']['post_no']    #楼层
            try:
                replyTime = data_field['content']['date']    #回复时间
            except Exception as e :
                aaa = floorItem('.d_post_content_main .core_reply .core_reply_tail .post-tail-wrap>.tail-info')
                replyTime = aaa.eq(2).text()


            #处理回复内容
            content = floorItem('.d_post_content_main .p_content cc .d_post_content')
            contentText = content.text().strip()
            contentImgList = content('img')
            imgUrlList = list()
            for contentItem in contentImgList.items():
                imgUrl = contentItem.attr('src')
                if imgUrl is not None and imgUrl !='':
                    imgUrlList.append(imgUrl)

            #创建帖子对象
            tieItem = TieItem()
            tieItem['tId'] = str(tId)
            tieItem['title'] = title
            tieItem['tieUrl'] = tieUrl
            tieItem['isOwner'] = isOwner
            tieItem['userId'] = str(userId)
            tieItem['username'] = str(username)
            tieItem['userHeadUrl'] = userHeadUrl
            tieItem['floor'] = str(floor)
            tieItem['replyTime'] = replyTime
            tieItem['content'] = contentText
            tieItem['contentImgUrls'] = json.dumps(imgUrlList) if imgUrlList is not None else '[]'
            tieItem['replyTime'] = replyTime
            tieItem['pId'] = str(pId)
            yield tieItem
            
