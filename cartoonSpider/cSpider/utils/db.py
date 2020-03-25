import pymysql
from twisted.enterprise import adbapi
from cartoonSpider.cSpider.utils.db_config import db_config

class DbPool:

    dbpool = None
    db_name = None


    def __init__(self,db_name=None):
        if db_name is not None:
            self.db_name = db_name
        else:
            self.db_name = db_config['MYSQL_DB']
        if self.dbpool is None:
            self.initDbPool()

    def initDbPool(self):
        db_parmars = {
            'host': db_config['MYSQL_HOST'],
            'db': self.db_name,
            'port': db_config['MYSQL_PORT'],
            'user': db_config['MYSQL_USER'],
            'passwd': db_config['MYSQL_PASSWORD'],
            'charset': db_config['MYSQL_CHARSET'],
            'cursorclass':pymysql.cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql', **db_parmars)

    def getDbPool(self):
        return self.dbpool

class MySqlHelper:
    conn = None
    db_name = None


    def __init__(self,db_name=None):
        if db_name is not None:
            self.db_name = db_name
        else:
            self.db_name = db_config['MYSQL_DB']
        if self.conn is None:
            self.initDbHelper()


    def initDbHelper(self):
        db_parmars = {
            'host': db_config['MYSQL_HOST'],
            'database': self.db_name,
            'port': db_config['MYSQL_PORT'],
            'user': db_config['MYSQL_USER'],
            'password': db_config['MYSQL_PASSWORD'],
            'charset': db_config['MYSQL_CHARSET'],
        }
        self.conn = pymysql.Connect(**db_parmars)  #数据库连接对象


    def getConn(self):
        return self.conn if self.conn is not None else None

    def close(self):
        if self.conn is not None:
            self.conn.close()

    #查询
    def query(self,sql,params):
        if self.conn is None:
            self.close()
            return None

        cursor = self.conn.cursor()
        lines = cursor.execute(sql,params)
        self.close()
        if lines > 0:
            return cursor.fetchall()
        else:
            return None