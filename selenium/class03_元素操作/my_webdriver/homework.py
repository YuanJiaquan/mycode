'''
    课后作业：
        1. 实现商城的注册与登录自动化流程
        请自行添加自己的账号密码
        商城URL：http://39.98.138.157/shopxo/index.php
        作业发我QQ邮箱
'''
from time import sleep
from may2.log.test.test2 import fen_log

from selenium import webdriver
log=fen_log()
driver=webdriver.Chrome()
log.info('初始化driver{}'.format(driver))
l1=driver.maximize_window()
log.info('放大window{}'.format(l1))
l2=driver.get('http://39.98.138.157/shopxo/index.php')
log.info('访问地址{}'.format('http://39.98.138.157/shopxo/index.php'))
sleep(2)
driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[2]/a[1]').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[1]/input').send_keys('_jiaquan07')
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[2]/input').send_keys('772878309quan')
driver.find_element_by_xpath().click()

sleep(5)
driver.close()