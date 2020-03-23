# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem
from cSpider.utils.db import DbPool


class CspiderPipeline(object):

    def __init__(self):
        self.dbpool = DbPool().getDbPool()




    def process_item(self, item, spider):
        if item['type'] == 1:
            self.deal_chapter(item)
        elif item['type'] == 2:
            self.deal_chapter_details(item)


    #处理章节
    def deal_chapter(self,item):
        if item is None or item['chapterUrl'] is None :
            raise DropItem("Missing chapterUrl")
        query = self.dbpool.runInteraction(
            self.insert_data_to_mysql,
            item
        )
        query.addErrback(
            self.insert_err,
            item
        )

    #处理每一页
    def deal_chapter_details(self,item):
        if item is None or item['imageUrl'] is None :
            raise DropItem("Missing chapterUrl")
        query = self.dbpool.runInteraction(
            self.insert_data_to_mysql,
            item
        )
        query.addErrback(
            self.insert_err,
            item
        )
        pass


    #插入
    def insert_data_to_mysql(self, cursor, item):
        sql = item.getInsertSql()
        data = item.getInsertData(item)
        cursor.execute(sql, data)

    def insert_err(self, failure, item):
        print(failure, '失败', item)
