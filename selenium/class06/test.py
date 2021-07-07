

from selenium import webdriver
from 配置.Chrome_options import Options

driver=webdriver.Chrome(options=Options().options_conf())
driver.get('http://www.baidu.com')


