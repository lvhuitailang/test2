from queue import Queue
import time
import threading


def get_detail_url(queue): #模拟爬取主页
    num=1
    while True:
        print('请求主页数据\n')
        # time.sleep(2) #模拟网络请求时间
        for i in range(20): #抓取20个链接  #put方法是队列满了会一直停滞
            queue.put('hettp://www.baidu.com/{id}'.format(id=num))
            num += 1
        print('主页数据记录完成\n')
        break

def get_detail_html(queue): #模拟爬取详情页
    while True:
        try:
            url = queue.get(block=False) #接受最后一个链接 #get方法是队列为空会一直停滞
            print('请求详情页数据:{url}\n'.format(url=url))
            # time.sleep(1)
            print('详情页数据记录完成\n')
        except Exception:
            break
if __name__ == "__main__":
    detail_url_queue=Queue(maxsize=1000)
    thread1 = threading.Thread(target = get_detail_url,args=(detail_url_queue,))
    thread1.start()
    start_time = time.time() #模拟时间
    for i in range(5):      #创建五个子线程。用于解析详情页
        thread_url = threading.Thread(target = get_detail_html,args=(detail_url_queue,))
        thread_url.start()
    print('用时:{0}'.format(time.time()-start_time))