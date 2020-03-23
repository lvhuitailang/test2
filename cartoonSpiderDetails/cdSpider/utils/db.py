import pymysql
from twisted.enterprise import adbapi
from cSpider.utils.db_config import db_config

class DbPool:

    dbpool = None


    def __init__(self):
        if self.dbpool is None:
            self.initDbPool(db_config)
        pass


    def initDbPool(self,db_config):
        db_parmars = {
            'host': db_config['MYSQL_HOST'],
            'db': db_config['MYSQL_DB'],
            'port': db_config['MYSQL_PORT'],
            'user': db_config['MYSQL_USER'],
            'passwd': db_config['MYSQL_PASSWORD'],
            'charset': db_config['MYSQL_CHARSET'],
            'cursorclass':pymysql.cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql', **db_parmars)

    def getDbPool(self):
        return self.dbpool
