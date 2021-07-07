'''
    1. 实现商品添加的流程自动化
        复制选中的行数，默认是一行，ctrl+d
        对于一些重复的代码能cv的就直接cv，不要每次都敲

'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from class06_options_webui.chrome_options import Options

# 添加的商品数量
number = '4'
driver = webdriver.Chrome(options=Options().conf_options())
driver.implicitly_wait(10)
driver.get('http://39.98.138.157/shopxo/index.php')

# 登录操作
driver.find_element('link text', '登录').click()
driver.find_element('name', 'accounts').send_keys('xuzhu666')
driver.find_element('name', 'pwd').send_keys('123456')
driver.find_element('xpath', '//button[text()="登录"]').click()

# 搜索手机商品：iPhone 6
driver.find_element('id', 'search-input').send_keys('手机')
driver.find_element('id', 'ai-topsearch').click()
driver.find_element('xpath', '//div[@class="items"]/a[1]').click()

# 切换到商品详情页
handles = driver.window_handles
driver.close()
driver.switch_to.window(handles[1])

# 添加商品属性：建议请添加强制等待。
driver.find_element('xpath', '//li[@data-value="套餐一"]').click()
sleep(1)
driver.find_element('xpath', '//li[@data-value="金色"]').click()
sleep(1)
driver.find_element('xpath', '//li[@data-value="64G"]').click()
sleep(1)
# 输入商品数量
el = driver.find_element('xpath', '//input[@id="text_box"]')
el.clear()
el.send_keys(number)
driver.find_element('xpath', '//button[@title="加入购物车"]').click()
# assert driver.find_element('xpath', '//p[text()="加入成功"]').text == '加入成功', '加入失败'

# 进入购物车页面，检查商品是否添加成功
driver.find_element('xpath', '//span[text()="购物车"]').click()
# 切换到购物车页面
# 查看商品是否存在
# WebDriverWait(driver, 5, 0.5).until(
#     lambda el: driver.find_element('xpath', '//div[@class="goods-base"]/a[1]'),
#     message='添加失败')
# 校验添加的商品数量与预期是否一致
assert driver.find_element('xpath', '//input[@type="number"]').get_attribute('value') == number, '数量不对'
