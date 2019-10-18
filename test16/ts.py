
import unittest
import ddt
from selenium import  webdriver
import time

test_data1 = [{"username": "zhangsan", "pwd": "zhangsan"},
              {"username": "lisi", "pwd": "lisi"},
              {"username": "wangwu", "pwd": "wangwu"},
              ]
# @ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print('111')
        # self.drvier=webdriver.Chrome()
        # url='http://www.cqhongyu.com:2222/admin/login'
        # self.drvier.get(url)
        # self.drvier.implicitly_wait(30)

    # def login(self,username,pwd):
    #     self.drvier.find_element_by_id('username').send_keys(username)
    #     self.drvier.find_element_by_name('password').send_keys(pwd)
    #     self.drvier.find_element_by_id('submit').click()
    #     time.sieep(3)
    #
    # def iscussess(self):
    #     text=self.drvier.find_element_by_xpath('//*[@id="userIcon"]').text
    #     return text

    #
    # @ddt.ddt(*test_data1)
    # def login_issucess(self,data):
    #     Test.login(ddt['username'],ddt['password'])
    #     result=Test.iscussess()
    #     self.assertTrue(result)


    # def tearDown(self):
    #     self.drvier.quit()

if __name__ == "__main__":
    unittest.main()

