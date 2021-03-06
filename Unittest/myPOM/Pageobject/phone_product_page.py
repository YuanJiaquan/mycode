'''
    手机商品详情页：PhonePage，主要显示手机的商品详情内容，用于执行对应的操作行为。
'''
from time import sleep

from selenium import webdriver



# 手机详情页
from Unittest.myPOM.Basepage.Basepage01 import BasePage01


class PhonePage(BasePage01):
    '''
        页面对象类的模版：
            1. url
            2. 关键元素
            3. 行为
    '''
    # url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/2.html'

    # 关键元素
    suite = ('xpath', '//li[@data-value="套餐一"]')
    color = ('xpath', '//li[@data-value="金色"]')
    memory = ('xpath', '//li[@data-value="128G"]')
    add_cart_button = ('xpath', '//button[@title="加入购物车"]')

    # 添加购物车行为
    def add_cart(self):
        # 访问页面
        self.visit(self.url)
        # 选择商品属性
        self.click(self.suite)
        sleep(1)
        self.click(self.color)
        sleep(1)
        self.click(self.memory)
        # 点击添加购物车
        self.click(self.add_cart_button)

    def check_info(self):
        self.visit(self.url)

    # 例如初审，包含审批通过或者审批不通过
    def check(self, type_):
        if type_ == '1':
            # 审批
            pass
        else:
            # 驳回
            pass


# 调试
if __name__ == '__main__':
    driver = webdriver.Chrome()
    pp = PhonePage(driver)
    pp.add_cart()
