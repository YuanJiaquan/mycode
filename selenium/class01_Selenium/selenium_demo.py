'''
    第一个Selenium的Demo演示：
    百度的搜索执行
'''
# 导入selenium模块
from time import sleep

from selenium import webdriver

# 启动浏览器:浏览器首字母要大写，还要添加()
driver = webdriver.Chrome()
# 访问url:一定要在url中添加http://这样的内容,如果不加会报错，必须加//
driver.get('http://www.baidu.com')
# 输入‘秋水好蠢’：通过find element函数查找元素，一定是查找有对应属性的元素
driver.find_element_by_name('wd').send_keys('秋水好蠢')
# 点击‘百度一下’按钮实现搜索
driver.find_element_by_id('su').click()
# 添加等待
sleep(3)
# 关闭浏览器并释放进程资源
driver.quit()
