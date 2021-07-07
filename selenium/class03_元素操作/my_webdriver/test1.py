from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver=WebDriver(executable_path="chromedriver")
driver.maximize_window()
driver.get('http://music.163.com')
# driver.implicitly_wait(10)
iframe=driver.find_element(By.ID,'g_iframe')
driver.switch_to.frame(iframe)
# iframe=driver.find_element_by_id('g_iframe')
# driver.switch_to.frame(iframe)
driver.find_element(By.XPATH,'//img[@class="d-flag"]').click()

sleep(3)
driver.close()