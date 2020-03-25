from queue import Queue
import time
import sys
import os
from concurrent.futures import ThreadPoolExecutor
import requests
from cartoonSpider.cSpider.utils.db import MySqlHelper


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}

GLOBAL_TITLE = '一人之下'
GLOBAL_ABAPATH = os.getcwd()#当前路径
GLOBAL_IMGPATH = GLOBAL_ABAPATH+'/imgs/'+GLOBAL_TITLE.strip()

if '__main__' == __name__:

    #创建文件夹用来存放文件
    if not os.path.exists(GLOBAL_IMGPATH):
        os.makedirs(GLOBAL_IMGPATH)

    mySqlHelper = MySqlHelper()

    sql = r'select cd.chapterTitle,cd.chapterSort,cd.page,cd.imageUrl from chapterdetail cd where cd.title="%s" order by CAST(cd.chapterSort AS UNSIGNED) asc' %(GLOBAL_TITLE,)
    result = mySqlHelper.query(sql,None)

    if not result:
        sys.exit(1)

    q = Queue(maxsize=0)    #0表示无穷大
    [q.put(chapterDetail,block=False) for chapterDetail in result]    #将所有的tieItem房间queue

    # while not q.empty():
    #     print(q.get())






    #下载文件
    def download(item):
        chapterTitle = item[0].strip()
        chapterSort = item[1].strip()
        page = item[2].strip()
        imageUrl = item[3].strip()



        if not imageUrl:
            return
        fileName = '-'.join((chapterSort,page,chapterTitle))+'.jpg'
        res = requests.get(url=imageUrl,headers=headers)
        with open(GLOBAL_IMGPATH+'/'+fileName,'wb') as f:
            f.write(res.content)
            print(fileName+'============写入成功')



    #开启线程下载
    with ThreadPoolExecutor(20) as executor:
        while not q.empty():
            executor.submit(download,q.get())

    #
    # download('111',r'https://imgsa.baidu.com/forum/w%3D580/sign=95fd75a48bd4b31cf03c94b3b7d7276f/7bb5c9ea15ce36d30a29edd73af33a87e950b12c.jpg')