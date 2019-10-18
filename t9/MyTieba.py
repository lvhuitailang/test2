import requests
from bs4 import BeautifulSoup
import re
def filterBlanks(text):
    """过滤文字中的空格，并将br转换成换行"""
    regex_filterBlanks = re.compile(r'\s+', re.S)
    text = re.sub(regex_filterBlanks, ' ', text)
    regex_transforBR = re.compile(r'<br>', re.S)
    text = re.sub(regex_transforBR, '\n', text)
    return text

class TieBa:
    """贴吧帖子抓取"""

    def __init__(self, url ,headers):
        """初始化"""
        self.url = url
        self.headers = headers


    def getPage(self):
        """获得页面"""
        if not hasattr(self, 'url') :
            print('init '+self.__class__.__name__+' first.')
            return None
        try:
            res = requests.get(self.url, headers=self.headers)
            if res.status_code == 200:
                self.soup = BeautifulSoup(res.text,'lxml')
                return res.text
            else:
                return None
        except BaseException as e:
            print(e)
            return None

    def getTieTitle(self):
        """获得帖子标题"""
        if not hasattr(self, 'soup'):
            print('请先配置self.soup')
            return None
        try:
            soup = self.soup
            title = soup.select(r'h3.core_title_txt')[0].get_text()
            return filterBlanks(title)
        except BaseException as e:
            print(e)
            return '[]'

    def getTotalPage(self):
        """获得总页数"""
        if not hasattr(self, 'soup'):
            print('请先配置self.soup')
            return None
        try:
            soup = self.soup
            totalPage = soup.select(r'ul.l_posts_num li.l_reply_num span.red')[1].get_text()
            return int(totalPage)
        except BaseException as e:
            print(e)
            return 1

    def getAllFloors(self):
        """获得所有楼层"""
        if not hasattr(self, 'soup'):
            print('请先配置self.soup')
            return None
        try:
            soup = self.soup
            allFloors = soup.select(r'div.l_post.l_post_bright.j_l_post.clearfix  ')
            return allFloors
        except BaseException as e:
            print(e)
            return list()

    def getUsernameFromFloor(self, floor):
        """获得一层楼的用户名"""
        try:
            username = floor.select(r'div.d_author ul.p_author li.d_name a')[0].get_text()
            return username
        except BaseException as e:
            print(e)
            return ''

    def getContentTextFromFloor(self, floor):
        """获得楼层文本"""
        try:
            text = floor.select(r'div.d_post_content_main  cc div.d_post_content.j_d_post_content  ')[0].get_text()
            return filterBlanks(text)
        except BaseException as e:
            print(e)
            return ''

    def getContentImgsFromFloor(self, floor):
        """获得楼层图片"""
        try:
            imgList = list()
            imgTagList = floor.find(r'cc').find_all(r'img')
            for item in imgTagList:
                if item['src']:
                    imgList.append(item['src'])
            return imgList
        except BaseException as e:
            print(e)
            return list()

    def getFloorNum(self, floor):
        """获得楼层号码"""
        try:
            floorNum = floor.select(r'div.core_reply_tail.clearfix div.post-tail-wrap>span')[2].get_text()
            return floorNum
        except BaseException as e:
            print(e)
            return -1


