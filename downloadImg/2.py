from queue import Queue
import time
import sys
from concurrent.futures import ThreadPoolExecutor
import requests
from downloadImg import settings as settings
import pymysql

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}

class MySqlHelper:
    def __init__(self):
        self.db_parmars = {
            'host': settings.MYSQL_HOST,
            'database': settings.MYSQL_DB,
            'port': settings.MYSQL_PORT,
            'user': settings.MYSQL_USER,
            'password': settings.MYSQL_PASSWORD,
            'charset': settings.MYSQL_CHARSET,
        }
        self.conn = pymysql.Connect(**self.db_parmars)  #数据库连接对象

    def getConn(self):
        return self.conn if self.conn is not None else None

    def close(self):
        if self.conn is not None:
            self.conn.close()

     #查询
    def query(self,sql,params):
        if self.conn is None:
            return None

        cursor = self.conn.cursor()
        lines = cursor.execute(sql,params)
        if lines > 0:
            return cursor.fetchall()
        else:
            return None


if '__main__' == __name__:

    mysqlHelper = MySqlHelper()
    sql = r'select pId,url,surl from fileUrlItem'
    allItems = mysqlHelper.query(sql,None)  #查询所有回复列表
    if not allItems:
        sys.exit(1)

    q = Queue(maxsize=0)    #0表示无穷大
    [q.put(tieItem,block=False) for tieItem in allItems]    #将所有的tieItem房间queue

    # while not q.empty():
    #     print(q.get())



    #下载文件
    def download(item):
        pId = item[0].strip()
        url = item[1].strip()
        surl = item[2].strip()
        downloadUrl = surl
        if surl:
            downloadUrl = surl
        elif url:
            downloadUrl = url
        else:
            downloadUrl = ''
        if not downloadUrl:
            return
        fileName = pId+downloadUrl[-10:]
        res = requests.get(url=downloadUrl,headers=headers)
        with open(r'img/'+fileName,'wb') as f:
            f.write(res.content)
            print(fileName+'============写入成功')



    #开启线程下载
    with ThreadPoolExecutor(20) as executor:
        while not q.empty():
            executor.submit(download,q.get())
    #
    #
    # download('111',r'https://imgsa.baidu.com/forum/w%3D580/sign=95fd75a48bd4b31cf03c94b3b7d7276f/7bb5c9ea15ce36d30a29edd73af33a87e950b12c.jpg')