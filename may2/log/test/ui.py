import time

from selenium import webdriver


# import logging.config

# 拿到配置文件
# logging.config.fileConfig('log.ini')
# # 拿到日志器
# log = logging.getLogger()
from may2 import log

from may2.log.test.test2 import fen_log

log=fen_log()
class BasePage1():
    # 想要把操作记录在日志文件中。调用日志中的级别
    def __init__(self, driver):
        log.info('初始化driver{}'.format(driver))
        self.driver = driver

    def open(self, url):
        log.info('正在访问网址{}'.format(url))
        self.driver.get(url)

    def locator(self, name, value):
        return self.driver.find_element(name, value)

    def on_input(self, name, value, txt):
        try:
            log.info('正在定位{}元素，元素值为{},输入的内容为{}'.format(name, value, txt))
            self.locator(name, value).send_keys(txt)
        except Exception as e:
            log.error('输入内容失败%s' % e)

    def on_click(self, name, value):
        try:
            log.info('正在定位{}元素，元素值为{},进行点击'.format(name, value))
            self.locator(name, value).click()
        except Exception as e:
            log.error('点击按钮失败%s' % e)

    def wait(self, t):
        log.info('正在等待')
        time.sleep(t)

    def close(self):
        log.info('关闭浏览器')
        self.driver.quit()
