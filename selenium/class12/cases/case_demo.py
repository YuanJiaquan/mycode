import unittest

from ddt import ddt, file_data
from selenium import webdriver

from class06.chrome_options import Options
from class12.page_object.login_page import LoginPage
from class12.page_object.product_page import ProductPage

'''
    如果你不希望用例之间产生关联。那就不同的流程，用不同的测试用例，将需要的页面对象分别实例化
    如果想快速的实现整个流程的覆盖测试，则通过一套driver全部实现
'''


@ddt
class Cases(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(options=Options().options_conf())
        cls.lp = LoginPage(cls.driver)
        cls.pg = ProductPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/user.yaml')
    def test_01_login(self, **kwargs):
        self.lp.login(kwargs['user'], kwargs['pwd'])

    def test_02_addcart(self):
        self.pg.addcart()


if __name__ == '__main__':
    unittest.main()
