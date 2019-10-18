# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tId = scrapy.Field() #帖子id(主键)
    title = scrapy.Field() #帖子标题
    tieUrl = scrapy.Field()#帖子链接
    isOwner = scrapy.Field()#是否是楼主

    userId = scrapy.Field()#层主id
    username = scrapy.Field()#层主名字
    userHeadUrl = scrapy.Field()#层主头像链接
    floor = scrapy.Field()#楼层
    replyTime = scrapy.Field()#回复时间
    content = scrapy.Field()#回复内容
    contentImgUrls = scrapy.Field()#回复图片链接
    pId = scrapy.Field()#暂定为回复的业务ID，每一条回复的唯一标识


    def getInsertSql(self):
        sql = '''
        replace into tieitem
        (tId,title,tieUrl,isOwner,userId,username,userHeadUrl,floor,replyTime,content,contentImgUrls,pId)
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
        return sql


    def getInsertData(self,item):
        data = (
            item['tId'],
            item['title'],
            item['tieUrl'],
            item['isOwner'],
            item['userId'],
            item['username'],
            item['userHeadUrl'],
            item['floor'],
            item['replyTime'],
            item['content'],
            item['contentImgUrls'],
            item['pId'],
        )
        return data



class FileUrlItem(scrapy.Item):
    url = scrapy.Field()
    surl = scrapy.Field()#  大图链接
    pId = scrapy.Field()
    tId = scrapy.Field()


    def getInsertSql(self):
        sql = '''
        replace into fileUrlItem
        (url,surl,pId,tId)
        values(%s,%s,%s,%s)
        '''
        return sql


    def getInsertData(self,item):
        data = (
            item['url'],
            item['surl'],
            item['pId'],
            item['tId'],

        )
        return data
