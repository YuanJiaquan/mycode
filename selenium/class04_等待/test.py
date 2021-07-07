

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()

driver.get('http://www.baidu.com')
driver.maximize_window()
WebDriverWait(driver,10).until( driver.find_element_by_id(), message='')




