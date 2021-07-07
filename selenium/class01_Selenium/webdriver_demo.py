'''
    从webdriver模块的底层代码应用来了解selenium+webdriver对浏览器进行交互的全部过程
'''
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver

# # 启动浏览器:浏览器首字母要大写，还要添加()
# driver = webdriver.Chrome()
wd = WebDriver(executable_path='chromedriver')
# # 访问url:一定要在url中添加http://这样的内容,如果不加会报错，必须加//
# driver.get('http://www.baidu.com')
# wd.execute('get', {'url': 'http://www.baidu.com'})
wd.get('http://www.baidu.com')
# # 输入‘秋水好蠢’：通过find element函数查找元素，一定是查找有对应属性的元素
# driver.find_element_by_name('wd').send_keys('秋水好蠢')
# el = wd.execute('findElement', {
#     'using': 'xpath',
#     'value': '//input[@id="kw"]'})['value']
# print(type(el))
# el._execute('sendKeysToElement', {
#     'text': '现在秋水聪明点了',
#     'value': ''
# })
wd.find_element_by_id('kw').send_keys('宝贝')

# # 点击‘百度一下’按钮实现搜索
# driver.find_element_by_id('su').click()
el = wd.execute('findElement', {
    'using': 'xpath',
    'value': '//input[@id="su"]'})['value']
print(type(el))
el._execute('clickElement')
# # 添加等待
sleep(3)
# # 关闭浏览器并释放进程资源
# driver.quit()
