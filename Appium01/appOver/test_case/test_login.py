# 测试登录  哪个知识点  uninttest/pytest

import unittest

# unittest必须要继承unittest.TestCase
from common.desired_caps import appium_desired
from page.loginpage import LoginView
from ddt import ddt,data,unpack,file_data

@ddt
class TestCase(unittest.TestCase):
    # 用例执行前做的事情  一个功能  流程 登录--选择商品--添加到购物车--下单
    # 启动程序
    def setUp(self) -> None:
        self.driver = appium_desired()

    def tearDown(self) -> None:
        self.driver.quit()

    # 跳过pytest.mark.skip
    # @unittest.skip('skip test_login')
    # def test_login(self):
    #     l=LoginView(self.driver)
    #     l.login('qwerty2664','qwerty123')

    @file_data('../data/login.yaml')
    def test_login2(self,uname,upass):
        l = LoginView(self.driver)
        l.login(uname,upass)
        self.assertTrue(l.login_status(),msg='登录失败')

#执行用例  测试一条数据   ddt  app自动化 toast  配置参数
# 选取一个位置 ，找到了这个位置就成功

# 检测  登录成功没有  在去写个方法
if __name__ == '__main__':
       unittest.main()


# 总结：
# 1.启动程序，常用的方法取消 跳过  写在公共文件  common
# 2.取消 跳过会用到 点击 找元素内容 简介 没有冗余  把基本的操作封装其阿里 baseView
# 3.登录页面  支付页面  流程页面  pom页面对象  页面元素 页面流程  一个个的页面里面
# 4.测试用例  测什么东西  登录  unittest/pytest 一个流程  函数里面 登录，选择商品
# 5.很多测试数据 data文件夹

# 页面元素和流程分开
# yaml文件