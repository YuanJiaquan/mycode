from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()


driver.get('http://www.msong.net/tv-type-id-2-pg-1.html')

driver.maximize_window()

# driver.implicitly_wait(30)
element = WebDriverWait(driver, 30, 0.5).until_not(
    lambda el: driver.find_element_by_xpath('/html/body/div[3]/div/ul[1]/li[4]/a/img'), message='查找元素失败')
driver.find_element(By.XPATH,'/html/body/div[3]/div/ul[1]/li[4]/a/img').click()