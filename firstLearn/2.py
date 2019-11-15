import MyTieba as mtb
import time
from threading import  Thread
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
from multiprocessing import Pool



# #初始化
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# myT = TieBa(r'https://tieba.baidu.com/p/3630743420?pn=1',headers)
# #获得页面
# html = myT.getPage()
# #获得标题
# title = myT.getTieTitle()
# #获得总页数
# totalPages = myT.getTotalPage()
# #获得所有楼层
# allFloors = myT.getAllFloors()
# #获得层主用户名
# floorUsername = myT.getUsernameFromFloor(allFloors[0])
# #获得楼层内容文本
# contentText = myT.getContentTextFromFloor(allFloors[0])
# #获得楼层内容图片
# contentImgs = myT.getContentImgsFromFloor(allFloors[0])
# print(contentImgs)

def getTiesOnePage(url,outMode = 'printAndSave'):
    # 初始化
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    myT = mtb.TieBa(url, headers)
    # 获得页面
    '''连接错误的时候进行重新尝试10次 start'''
    html = myT.getPage()
    count = 0
    while count < 10 and html is None:
        html = myT.getPage()
        count += 1
        time.sleep(5)
        print('retry : ',str(count)+'th time ...')

    if html is None:
        print('I tried 10 times to connect, but failed, program exited ...')
        return
    '''连接错误的时候进行重新尝试10次 end'''


    def printRes(string):
        """ 打印"""
        print(string)

    def saveToFile(fileName,data):
        """ 保存到文件"""
        with open(fileName,mode='a+',encoding='utf-8') as f:
            f.write(data)
            f.flush()
            f.close()

    #获得所有楼层
    allFloors = myT.getAllFloors()
    #遍历处理每层楼
    for i,floor in enumerate(allFloors):
        floorNum = -1
        floorNum = myT.getFloorNum(floor)
        if floorNum == -1:
            continue
        str_ = ''
        str_ += '楼层: '+str(floorNum)+'\n'
        str_ += '层主: '+myT.getUsernameFromFloor(floor)+'\n'
        str_ += '内容: '+myT.getContentTextFromFloor(floor)+'\n'
        imgList = myT.getContentImgsFromFloor(floor)
        if len(imgList) > 0:
            str_ += '相关图片: '+'\n\t\t '.join(myT.getContentImgsFromFloor(floor))+'\n'

        str_ += '=================================================\n'

        #输出模式
        if outMode == 'print':
            printRes(str_)
        elif outMode == 'save':
            saveToFile('./saves/file.txt',str_)
        elif outMode == 'printAndSave':
            printRes(str_)
            saveToFile('./saves/file.txt',str_)



#普通单线程运行
def go(page, totalPages):

    startTime = time.time()
    while page <= totalPages:
        getTiesOnePage(url='https://tieba.baidu.com/p/3630743420?pn='+str(page),outMode='printAndSave')
        page += 1
    endTime = time.time()
    duringTime = endTime - startTime
    print(duringTime)

#普通多线程运行
def multThread(page, totalPages):

    class MyThread(Thread):
        def __init__(self,page):
            super(MyThread, self).__init__()
            self.page = page
            self.start()

        def run(self):
            print('Thread: '+str(self.page)+' is running')
            getTiesOnePage('https://tieba.baidu.com/p/3630743420?pn=' + str(self.page), outMode='printAndSave')

    startTime = time.time()
    tList = list()
    for i in range(totalPages):
        t = MyThread(i+1)
        tList.append(t)

    for item in tList:
        item.join()
    endTime = time.time()
    duringTime = endTime - startTime
    print('\n耗时: '+str(duringTime)+'\n')
    print('done')

#ThreadPoolExecutor 线程池方式多线程
def goThreadPoolExecutor(page, totalPages):
    startTime = time.time()
    with ThreadPoolExecutor(totalPages) as executor:
        for x in range(totalPages):
            executor.submit(getTiesOnePage,url='https://tieba.baidu.com/p/3630743420?pn=' + str(x+1), outMode='printAndSave')

    endTime = time.time()
    duringTime = endTime - startTime
    print('\n耗时: ' + str(duringTime) + '\n')

#普通多进程
def goNormalProcess(page, totalPages):
    startTime = time.time()
    for x in range(totalPages):
        p = Process(target=getTiesOnePage,args=('https://tieba.baidu.com/p/3630743420?pn=' + str(x+1), 'save'))
        p.start()
       # p.join()
        print(str(x)+' :process end...')
    endTime = time.time()
    duringTime = endTime - startTime
    print('\n耗时: ' + str(duringTime) + '\n')

#Pool进程池多进程
def goPoolProcess(page, totalPages):


    pool = Pool(10)
    startTime = time.time()
    for x in range(totalPages):
        pool.map(getTiesOnePage,('https://tieba.baidu.com/p/3630743420?pn=' + str(x+1) for x in range(totalPages)))
    pool.close()
    endTime = time.time()
    duringTime = endTime - startTime
    print('\n耗时: ' + str(duringTime) + '\n')

if __name__ == '__main__':
    # 初始化
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    myT = mtb.TieBa(r'https://tieba.baidu.com/p/3630743420?pn=1', headers)
    #获得页面(必须先进行此操作)
    html = myT.getPage()
    if html is None:
        print('连接出现问题 ...程序结束')
        exit()

    # 获得总页数
    totalPages = myT.getTotalPage()
    #当前页
    page = 1

    #单线程运行
    #go(page, 10)
    #普通多线程运行
    #multThread(page, 10)
    #ThreadPoolExecutor 线程池方式多线程
    goThreadPoolExecutor(page, totalPages)
    # 普通多进程
    #goNormalProcess(page, 10)
    #进程池多进程
    #goPoolProcess(page, 10)


