from selenium import webdriver
from time  import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
# handle = driver.current_window_handle
driver.get('https://music.163.com')
# driver.get('https://www.baidu.com')
sleep(3)
el = driver.find_element(By.LINK_TEXT,'登录')
el.click()
sleep(3)
el = driver.find_element(By.LINK_TEXT,'选择其他登录模式')
el.click()
sleep(3)
driver.find_element(By.XPATH,'//*[@id="j-official-terms"]').click()
el1=driver.find_element(By.XPATH,'//a[@href="https://music.163.com/api/sns/authorize?snsType=5&clientType=web2&callbackType=Login&forcelogin=true"]')
el1.click()
sleep(2)
handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[1])
iframe=driver.find_element_by_id('ptlogin_iframe')
driver.switch_to.frame(iframe)
sleep(2)
driver.find_element(By.XPATH,'//a[@id="switcher_plogin"]').click()
print(driver.title)
sleep(2)
driver.find_element_by_id('u').send_keys('772878309')
driver.find_element_by_id('p').send_keys(',0506quan')
driver.find_element_by_id('login_button').click()




