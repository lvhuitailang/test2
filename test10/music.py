
import urllib.request
import requests
import os

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class HttpSvc():
        """docstring for HttpSvc"""

        def __init__(self):
                super(HttpSvc, self).__init__()
                if not os.path.exists("d:/music"):
                        os.mkdir('d:/music')

        def get(self,values):

                print(len(values))

                # downNum    = 0
                #
                # for x in values:
                #         if not os.path.exists("d:/music/" + x['name'] + '.mp3'):
                #                 print('***** ' + x['name'] + '.mp3 ***** Downloading...')
                #                 url = 'http://music.163.com/song/media/outer/url?id=' + x['id'] + '.mp3'
                #                 try:
                #                         urllib.request.urlretrieve(url,'d:/music/' + x['name'].replace('/','') + '.mp3')
                #                         downNum = downNum + 1
                #                 except:
                #                         x = x - 1
                #                         print('Download wrong~')
                # print('Download complete ' + str(downNum) + ' files !')
                # # pass

        def getMusicData(self,url):

                #这里调用谷歌浏览器，就不需要设置请求头了
                # user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
                # headers    = {'User-Agent':user_agent}

                chrome_options=Options()
                #设置chrome浏览器无界面模式
                chrome_options.add_argument('--headless')
                browser = webdriver.Chrome(chrome_options=chrome_options)

                #webData    = requests.get(url,headers=headers).text

                #开始请求
                browser.get(url)
                #查找歌曲列表所在的iframe
                iframe = browser.find_element_by_id('g_iframe')
                browser.switch_to.frame(iframe)
                webData = browser.page_source

                #关闭浏览器
                browser.close()
                #关闭chreomedriver进程
                browser.quit()
                #后面就直接用bs4的操作了
                soup       = BeautifulSoup(webData,'lxml')
                # 列表
                musicTrList = soup.select(r'.m-table tbody tr')
                #find_list  = soup.find('ul',class_="f-hide").find_all('a')

                tempArr = []
                for musicItem in musicTrList:
                        music_id = musicItem.select(r'div.hd span.ply')[0].attrs['data-res-id']
                        music_name = musicItem.select(r'div.f-cb .ttc span b')[0].attrs['title']
                        # music_id  = a['href'].replace('/song?id=','')
                        # music_name = a.text
                        tempArr.append({'id':music_id,'name':music_name})
                return tempArr

if __name__ == '__main__':

        url1 = r'https://music.163.com/playlist?id=2074950566'
        url2 = r'https://music.163.com/#/playlist?id=59015966'
        newHttp = HttpSvc()
        musicData = newHttp.getMusicData(url2) #获取歌单歌曲id https://music.163.com/playlist?id=2074950566
        for i in musicData:
                print(i)
        #print(musicData)
        print(newHttp.get(musicData))