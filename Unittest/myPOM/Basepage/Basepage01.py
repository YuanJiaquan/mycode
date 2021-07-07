from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage01():
    def __init__(self,driver):
        self.driver=driver
        driver.implicitly_wait(10)


    def visit(self,url):
        self.driver.get(url)


    def locator(self, loc):
        # self.driver.forward()
        return self.driver.find_element(*loc)

    def input(self, loc,txt):
        self.locator(loc).send_keys(txt)


    def click(self,loc):
        self.locator(loc).click()

    def wait(self, loc):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locator(loc), message='等待失败')

    def assert_text(self):
        pass

    def quite(self):
        self.driver.quit()
