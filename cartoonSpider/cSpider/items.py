# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CartoonChapter(scrapy.Item):
    '''
    type:类型，1表示章节，2表示详情
    '''
    type = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    chapterTitle = scrapy.Field()
    chapterUrl = scrapy.Field()




    def getInsertSql(self):
        sql = '''
        insert into chapter
        (title,chapterTitle,chapterUrl)
        values(%s,%s,%s)
        '''
        return sql

    def getInsertData(self,item):
        data = (
            item['title'],
            item['chapterTitle'],
            item['chapterUrl'],

        )
        return data


class CspiderItemDetail(scrapy.Item):
    '''
   type:类型，1表示章节，2表示详情
   '''
    type = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    chapterId = scrapy.Field()
    chapterTitle = scrapy.Field()
    chapterUrl = scrapy.Field()
    page = scrapy.Field()


    def getInsertSql(self):
        sql = '''
        insert into chapter
        (title,chapterId,chapterTitle,chapterUrl)
        values(%s,%s,%s,%s)
        '''
        return sql

    def getInsertData(self,item):
        data = (
            item['title'],
            item['chapterId'],
            item['chapterTitle'],
            item['chapterUrl'],

        )
        return data