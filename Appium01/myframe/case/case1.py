import unittest


from  ddt import ddt,file_data
from Appium01.myframe.BaseView.BaseView import baseClass
from Appium01.myframe.config.config import config

@ddt
class testMysuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('测试开始','*'*30)
    @classmethod
    def tearDownClass(cls) -> None:
        print('测试结束','*'*30)

    def setUp(self) -> None:
        print('本用例测试开始')
    def tearDown(self) -> None:
        print('本用例测试结束')

    @file_data('../data/selector.yaml')
    def test01(self,**kwargs):
        print(kwargs['xpath'])


    def test02(self):
        driver = config()
        bc = baseClass(driver)
        bc.check_cancel(id='android:id/button2')
        bc.check_skip(xpath='//*[@resource-id="com.tal.kaoyan:id/tv_skip"]')
        bc.input('jiaquan0729','xpath','//*[@text="请输入用户名"]')
        bc.input('772878309quan','xpath','//*[@resource-id="com.tal.kaoyan:id/login_password_edittext"]')
        bc.click('xpath','//*[@text="登录"]')
        bc.checkinfo('xpath','//*[@text="确定"]')

    @file_data('../data/login.yaml')
    def test03(self,**kwargs):
        driver=config()
        bc=baseClass(driver)
        bc.check_cancel(id='android:id/button2')
        bc.check_skip(xpath='//*[@resource-id="com.tal.kaoyan:id/tv_skip"]')
        bc.input(kwargs['uname'],'xpath','//*[@text="请输入用户名"]')
        bc.input(kwargs['upass'],'xpath','//*[@resource-id="com.tal.kaoyan:id/login_password_edittext"]')
        bc.click('xpath','//*[@text="登录"]')
        bc.checkinfo('xpath','//*[@text="确定"]')



if __name__ == '__main__':
    unittest.main()



