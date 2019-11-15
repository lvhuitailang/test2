import re
import requests

class MyCnnection:
    '''我的连接对象'''
    def __init__(self, url ,headers):
        """初始化"""
        self.url = url
        self.headers = headers


    def post(self,data):
        res = requests.post(self.url, headers=self.headers,data=data)
        print(res.status_code)



if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

    MyCnnection('http://211.149.197.67:8808/crm/admin/login',headers).post(data=dict(username='ls',password='123456'))




