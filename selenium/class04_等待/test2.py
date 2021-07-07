from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# 隐式等待
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('http://www.baidu.com')

driver.find_element('id', 'kw').send_keys('xuzhu')
driver.find_element('id', 'su').click()

# 强制等待
# sleep(2)

# 显式等待
el = WebDriverWait(driver, 10, 0.5).until(
    lambda el1: driver.find_element('xpath', '//*[@id="1"]/h3/a'), message='查找失败')

# WebDriverWait(driver, 5, 0.5).until_not(
#     lambda el1: driver.find_element('xpath', '//*[@id="1"]/h3/a'), message='查找失败')
driver.find_element('xpath', '//*[@id="1"]/h3/a').click()

