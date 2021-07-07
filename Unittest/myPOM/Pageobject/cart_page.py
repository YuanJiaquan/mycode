'''
    CartPage:购物车页面，校验商品是否添加成功
'''


# 购物车页面
from selenium import webdriver

from Unittest.myPOM.Basepage.Basepage01 import BasePage01


class CartPage(BasePage01):
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/cart/index.html'

    goods = ('xpath', '//a[contains(text(),"iPhone")]')

    # 校验商品是否存在
    def cart_info(self):
        self.visit(self.url)
        # return self.assert_text(self.goods, 'iPhone')
        self.wait(self.goods)


if __name__ == '__main__':
    driver=webdriver.Chrome()
    cc=CartPage(driver)
    cc.cart_info()
