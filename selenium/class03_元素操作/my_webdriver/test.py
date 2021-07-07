from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://music.163.com')
# iframe=driver.find_element_by_id('g_iframe')
# driver.switch_to.frame(iframe)
driver.find_element(By.XPATH,'//*[@id="g-topbar"]/div[1]/div/ul/li[4]/span/a').click()
handles=driver.window_handles
print(handles)
driver.switch_to.window(handles[1])
sleep(2)
driver.find_element_by_xpath('//*[@id="digital-counter"]/div/a[2]/i').click()
sleep(5)
driver.close()
handles=driver.window_handles
print(handles)
driver.switch_to.window(handles[0])

# driver.switch_to.frame(iframe)
# driver.switch_to.default_content()
sleep(2)
driver.find_element_by_xpath('//*[@id="discover-module"]/div[1]/div/div/div[1]/ul/li[1]/div/a').click()
sleep(2)
driver.find_element(By.XPATH,'//*[@id="content-operation"]/a[1]').click()

sleep(2)



