import pymysql
from twisted.enterprise import adbapi
from cSpider.utils.db_config import db_config

class DbPool:

    dbpool = None
    db_name = None


    def __init__(self,db_name=None):
        if self.dbpool is None:
            self.initDbPool(db_config)
        if db_name is not None:
            self.db_name = db_name
        pass


    def initDbPool(self,db_config):
        db_name_temp =  db_config['MYSQL_DB'] if self.db_name is None  else  self.db_Name
        db_parmars = {
            'host': db_config['MYSQL_HOST'],
            'db': db_name_temp,
            'port': db_config['MYSQL_PORT'],
            'user': db_config['MYSQL_USER'],
            'passwd': db_config['MYSQL_PASSWORD'],
            'charset': db_config['MYSQL_CHARSET'],
            'cursorclass':pymysql.cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql', **db_parmars)

    def getDbPool(self):
        return self.dbpool
