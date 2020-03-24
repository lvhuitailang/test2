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


class Chapter(scrapy.Item):
    '''
    type:类型，1表示章节，2表示详情
    '''
    id = scrapy.Field()
    title = scrapy.Field()
    sort = scrapy.Field()
    type = scrapy.Field()
    chapterTitle = scrapy.Field()
    chapterUrl = scrapy.Field()




    def getInsertSql(self):
        sql = '''
        insert into chapter
        (title,sort,type,chapterTitle,chapterUrl)
        values(%s,%s,%s,%s,%s)
        '''
        return sql

    def getInsertData(self,item):
        data = (
            item['title'],
            str(item['sort']),
            str(item['type']),
            item['chapterTitle'],
            item['chapterUrl'],

        )
        return data


class ChapterDetail(scrapy.Item):
    '''
   type:类型，1表示章节，2表示详情
   '''
    id = scrapy.Field()
    title = scrapy.Field()
    type = scrapy.Field()
    chapterId = scrapy.Field()
    chapterSort = scrapy.Field()
    chapterTitle = scrapy.Field()
    chapterUrl = scrapy.Field()
    page = scrapy.Field()
    pageUrl = scrapy.Field()
    imageUrl = scrapy.Field()


    def getInsertSql(self):
        sql = '''
        insert into chapterDetail
        (title,type,chapterId,chapterSort,chapterTitle,chapterUrl,page,pageUrl,imageUrl)
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
        return sql

    def getInsertData(self,item):
        data = (
            item['title'],
            str(item['type']),
            item['chapterId'],
            str(item['chapterSort']),
            item['chapterTitle'],
            item['chapterUrl'],
            str(item['page']),
            item['pageUrl'],
            item['imageUrl'],

        )
        return data