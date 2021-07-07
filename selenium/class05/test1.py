from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')

el = driver.find_element('xpath', '//span[text()="设置"]')
actions=ActionChains(driver)
actions.move_to_element(el).perform()
driver.find_element('link text', '搜索设置').click()
driver.save_screenshot('1.png')
