'''
    补课： 元素悬停
        from selenium.webdriver import ActionChains
        通过ActionChains模块来实现
'''
from selenium import webdriver
from selenium.webdriver import ActionChains

from class06.chrome_options import Options

# driver = webdriver.Chrome(options=Options().options_conf())
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com/')
# 悬停操作：在执行过程中鼠标不能动
el = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
action = ActionChains(driver)
action.move_to_element(el).perform()
# driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click()
