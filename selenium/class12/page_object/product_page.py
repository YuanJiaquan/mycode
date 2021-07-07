from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from class12.base.base_page import BasePage


class ProductPage(BasePage):
    url = BasePage.url + '?s=/index/goods/index/id/2.html'

    suite = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[1]/ul/li[2]')
    color = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[2]/ul/li[2]')
    memory = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[3]/ul/li[2]')
    cart = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/button')

    def addcart(self):
        self.open()
        self.click(self.suite)
        sleep(1)
        self.click(self.color)
        sleep(1)
        self.click(self.memory)
        sleep(1)
        self.click(self.cart)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    pg = ProductPage(driver)
    pg.addcart()
