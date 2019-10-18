import unittest
import ddt
from selenium import  webdriver
import time



list = [{'username':'zhangsan','pwd':'zhangsan'},{'username':'lisi','pwd':'lisi'},{'username':'wangwu','pwd':'wangwu'}]

driver = None
@ddt.ddt
class TestFunc(unittest.TestCase):

    # TestCase基类方法,所有case执行之前自动执行
    @classmethod
    def setUpClass(cls):
        print("这里是所有测试用例前的准备工作\n")
        global driver
        if driver is None:
            drvier=webdriver.Chrome()
            url='http://www.cqhongyu.com:2222/admin/login'
            drvier.get(url)
            drvier.implicitly_wait(30)
            print('浏览器打开成功\n')

    #打开浏览器并且跳转到指定url
    def setUp(self):
        pass



    @ddt.data(*list)
    @ddt.unpack
    def test_login(self,username,pwd):
        print(username+'  :  '+pwd+'\n')
        # self.drvier.find_element_by_id('username').send_keys(username)
        # self.drvier.find_element_by_name('password').send_keys(pwd)
        # self.drvier.find_element_by_id('submit').click()
        # time.sieep(3)

    # @ddt.data(*list)
    # @ddt.unpack
    # def test_list(self, username, pwd):
    #     print(username, pwd)


if __name__ == '__main__':
    unittest.main()  # 开始调用

