# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi

class TieBaListPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        db_parmars = {
            'host': settings['MYSQL_HOST'],
            'db': settings['MYSQL_DB'],
            'port': settings['MYSQL_PORT'],
            'user': settings['MYSQL_USER'],
            'passwd': settings['MYSQL_PASSWORD'],
            'charset': settings['MYSQL_CHARSET'],
            'cursorclass':pymysql.cursors.DictCursor
        }
        dbpool = adbapi.ConnectionPool('pymysql', **db_parmars)
        return cls(dbpool)


    def process_item(self, item, spider):
        if item is None or item['tId'] is None or item['tId'] == '' or item['tId'] == 'null':
            raise DropItem("Missing tId")
        query = self.dbpool.runInteraction(
            self.insert_data_to_mysql,
            item
        )
        query.addErrback(
            self.insert_err,
            item
        )

        return item


    #插入
    def insert_data_to_mysql(self, cursor, item):
        sql = item.getInsertSql()
        data = item.getInsertData(item)
        cursor.execute(sql, data)

    def insert_err(self, failure, item):
        print(failure, '失败', item)
