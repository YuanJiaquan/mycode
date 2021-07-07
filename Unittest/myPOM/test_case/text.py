


import unittest
from time import sleep

from selenium import webdriver



from Unittest.myPOM.Pageobject.cart_page import CartPage
from Unittest.myPOM.Pageobject.login import Login
from Unittest.myPOM.Pageobject.phone_product_page import PhonePage


class test(unittest.TestCase):


    def test(self):
        driver = webdriver.Chrome()
        lp = Login(driver)
        sleep(5)
        pp = PhonePage(driver)
        sleep(5)
        cp = CartPage(driver)
        user = 'xuzhu666'
        pwd = '123456'
        lp.login(user, pwd)
        pp.add_cart()
        cp.cart_info()
        print('执行成功')
        sleep(5)
        driver.quit()

if __name__ == '__main__':
    unittest.main()
