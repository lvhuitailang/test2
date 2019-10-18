import unittest
import test15.HTMLTestRunner as HTMLTestRunner
def add(a, b):
    return a+b

def minus(a, b):
    return a-b

def multi(a, b):
    return a*b

def divide(a, b):
    return a/b


class TestMathFunc(unittest.TestCase):

    # TestCase基类方法,所有case执行之前自动执行
    @classmethod
    def setUpClass(cls):
        print("这里是所有测试用例前的准备工作")

    # TestCase基类方法,所有case执行之后自动执行
    @classmethod
    def tearDownClass(cls):
        print("这里是所有测试用例后的清理工作")

    # TestCase基类方法,每次执行case前自动执行
    def setUp(self):
        print("这里是一个测试用例前的准备工作")

    # TestCase基类方法,每次执行case后自动执行
    def tearDown(self):
        print("这里是一个测试用例后的清理工作")

    @unittest.skip("跳过这个测试用例.")
    def test_add(self):
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))  # 测试业务方法add

    def test_minus(self):
        self.skipTest('跳过这个测试用例')
        self.assertEqual(1, minus(3, 2))  # 测试业务方法minus

    def test_multi(self):
        self.assertEqual(6, multi(2, 3))  # 测试业务方法multi

    def test_divide(self):
        self.assertEqual(2, divide(6, 3))  # 测试业务方法divide
        self.assertEqual(2.5, divide(5, 2))

if __name__ == '__main__':
    unittest.main()  # 开始调用
    # # suite = unittest.TestSuite()
    # # suite.addTest(TestMathFunc('test_multi'))
    # filename = 'TEST.html'
    # fb = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title="测试HTMLTestRunner", description="测试HTMLTestRunner")
    # runner.run(unittest.main())
