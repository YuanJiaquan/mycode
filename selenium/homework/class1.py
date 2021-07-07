from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
wd=WebDriver(executable_path="chromedriver")
# 创建浏览器对象
wd.get('http://www.baidu.com')
# 调用WebDriver继承的RemoteWebDriver class类内部的get函数，对浏览器进行访问网址操作
wd.find_element_by_id('kw').send_keys('宝贝')
# 元素定位并输入值
wd.find_element_by_id('su').click()
# 元素点击操作
sleep(3)
wd.quit()

