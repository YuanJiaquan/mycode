# 通过自动化测试行为，实现电商的下单流程。
# 登录-搜索商品-添加商品属性-加入购物车-校验购物车是否添加成功
# 推荐使用商品是手机，iPhone 6
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(1)
driver.maximize_window()
driver.get('http://39.98.138.157/shopxo/index.php')
# 点击登录
driver.find_element(By.XPATH,'//a[@class="am-btn-primary btn am-fl"]').click()
# 输入登录信息并且登录
driver.find_element(By.XPATH,'//input[@placeholder="用户名/手机/邮箱"]').send_keys('_jiaquan07')
driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/form/div[2]/input').send_keys('772878309quan')
driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()

# 选择IPhone
WebDriverWait(driver,10).until(
    lambda el:driver.find_element(By.XPATH,'//*[@id="floor1"]/div[2]/div[2]/div[7]/a/img'),message='未找到该元素'
)
driver.find_element(By.XPATH,'//*[@id="floor1"]/div[2]/div[2]/div[7]/a/img').click()

handles=driver.window_handles
driver.switch_to.window(handles[1])
# 选择套餐
driver.find_element(By.XPATH,'//li[@data-value="套餐一"]').click()
WebDriverWait(driver,10).until(
    lambda el:driver.find_element(By.XPATH,'//li[@data-value="银色"]'),message='未找到该元素'
)
driver.find_element(By.XPATH,'//li[@data-value="银色"]').click()
driver.find_element(By.XPATH,'//li[@data-value="银色"]').click()
driver.find_element(By.XPATH,'//li[@data-value="32G"]').click()
driver.find_element(By.XPATH,'//li[@data-value="32G"]').click()

driver.find_element(By.XPATH,'//button[@title="点此按钮到下一步确认购买信息"]').click()

WebDriverWait(driver,10).until(
    lambda el:driver.find_element(By.XPATH,'//button[@title="点击此按钮，提交订单"]'),message='未找到该元素'
)
driver.find_element(By.XPATH,'//button[@title="点击此按钮，提交订单"]').click()