# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#帖子列表
class TieBaList(scrapy.Item):
    tId = scrapy.Field()
    reply = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    author = scrapy.Field()
    authorId = scrapy.Field()
    lastReplyName = scrapy.Field()
    lastReplyContent = scrapy.Field()
    lastReplyTime = scrapy.Field()
    tieUrl = scrapy.Field()

    def getInsertSql(self):
        sql = '''
        replace into tielist
        (tId,reply,title,info,author,authorId,lastReplyName,lastReplyContent,lastReplyTime,tieUrl)
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
        return sql

    def getInsertData(self,item):
        data = (
            item['tId'],
            item['reply'],
            item['title'],
            item['info'],
            item['author'],
            item['authorId'],
            item['lastReplyName'],
            item['lastReplyContent'],
            item['lastReplyTime'],
            item['tieUrl'],
        )
        return data

