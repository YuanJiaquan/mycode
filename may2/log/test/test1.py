
from selenium import webdriver

from may2.log.test.ui import BasePage1

driver=BasePage1(webdriver.Chrome())
driver.open('http://www.baidu.com')
driver.on_input('id','kw','秋水')
driver.on_click('id','su')
driver.wait(3)
driver.on_click('xpath','//*[@id="1"]/h3/a/em')
driver.wait(3)
driver.close()