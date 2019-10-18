import re
from urllib import request
from urllib import error as urlError


class MyCnnection:
    '''我的连接对象'''
    def __init__(self,url):
        self.url = url
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        self.req = request.Request(url=self.url,headers=self.headers)


    def getResNoCookie(self):
        '''获得页面'''
        try:
            self.requ = request.urlopen(self.req)
            return self.requ.read().decode('utf-8')
        except urlError as e:
            if hasattr(e,'code'):
                print(e.code)
            if hasattr(e,'reason'):
                print(e.reason)

    def getFloors(self,html):
        '''获得楼层'''
        regex_ = re.compile(r'<div\s+class="l_post l_post_bright j_l_post clearfix\s*"[^>]*>(.*?)\s*</div>\s*</div>\s*</div>\s*</div>',re.S)
        res = re.findall(regex_,html)
        return res

    def getContentFromFloor(self,floor):
        '''根据某个楼层获得帖子内容(包括图片和文字),没有内容返回None'''
        regex_ = re.compile(r'<cc>.*?<div.*?<div[^>]*?>\s*(.*?)</div>.*?<br>.*?</cc>',re.S)
        content = re.search(regex_,floor)
        if(content is None or content.lastindex != 1):
            return None
        else:
            return content.group(1)

    def getImgsFromContentItem(self,contentItem):
        '''从一层楼获取图片'''
        regex_ = re.compile(r'<img\s*class="BDE_Image".*?src="(.*?(?:\.jpg|\.gif|\.png))"\s*?pic_ext',re.S)
        imgList = re.findall(regex_,contentItem)
        return imgList
    def filterContentItemImgs(self,contentItem):
        '''过滤内容img，a标签'''
        regex_ = re.compile(r'(<img.*?>|<a.*?</a>)',re.S)
        contentText = re.sub(regex_,'',contentItem)
        return contentText

    def filterBlanks(self,contentText):
        '''过滤文字中的空格，并将br转换成换行'''
        regex_filterBlanks = re.compile(r'\s+',re.S)
        resultText = re.sub(regex_filterBlanks,' ',contentText)
        regex_transforBR = re.compile(r'<br>',re.S)
        resultText = re.sub(regex_transforBR,'\n',resultText)
        return resultText

    def getTotalPage(self,html):
        '''获得总的分页数量'''
        regex_ = re.compile(r'回复贴，共.*?<span class="red">(.*?)</span>.*?页',re.S)
        totalPage = re.search(regex_,html)
        if totalPage.lastindex == 1:
            return totalPage.group(1)
        else:
            return 1


#批量获取所有页的回复楼层
def getAll(url,totalPage=1):
    '''获取所有'''
    page = 1
    while page <= totalPage:
        #打开连接
        myconn = MyCnnection(url+'?pn='+str(page))
        # 得到页面
        html = myconn.getResNoCookie()
        # 获得当前页所有楼层
        floors = myconn.getFloors(html)
        for item in floors:
            # 根据一层楼获得内容(包括图片和文字)
            contentItem = myconn.getContentFromFloor(item)
            # 获得内容图片
            imgList = myconn.getImgsFromContentItem(contentItem)
            # 过滤内容img，a标签
            contentText = myconn.filterContentItemImgs(contentItem)
            # 去除内容文字中的多余空格并替换<br>回车
            resutText = myconn.filterBlanks(contentText)
            if(not imgList is None and len(imgList) > 0):
                print('相关图片: ',imgList)
            print(resutText,end='\n====================\n')
        page = page+1

#初始化连接
myconn = MyCnnection('https://tieba.baidu.com/p/3630743420')
#得到页面
html = myconn.getResNoCookie()
#获得总页数
totalPage = myconn.getTotalPage(html)


getAll(r'https://tieba.baidu.com/p/3630743420',10)

#
# for item in floors:
#     # 根据一层楼获得内容(包括图片和文字)
#     contentItem = myconn.getContentFromFloor(item)
#     # 获得内容图片
#     imgList = myconn.getImgsFromContentItem(contentItem)
#     # 过滤内容img，a标签
#     contentText = myconn.filterContentItemImgs(contentItem)
#     # 去除内容文字中的多余空格并替换<br>回车
#     resutText = myconn.filterBlanks(contentText)
#     if(not imgList is None and len(imgList) > 0):
#         print('相关图片: ',imgList)
#     print(resutText,end='\n====================\n')
