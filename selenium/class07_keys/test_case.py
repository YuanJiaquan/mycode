'''
    基于关键字驱动类实现的测试用例
'''

from class07_keys.web_keys import WebKey

# 测试用例1：实现电商的登录
# wk = WebKey('Chrome')
# wk.visit('http://39.98.138.157/shopxo/index.php')
# wk.click('link text', '登录')
# wk.input('name', 'accounts', 'xuzhu666')
# wk.input('name', 'pwd', '123456')
# wk.click('xpath', '//button[text()="登录"]')
# wk.sleep(3)
# wk.quit()

# 测试用例2: 百度搜索
wk = WebKey('Chrome')
wk.visit('http://www.jd.com')
wk.input('id', 'key', '笔记本')
wk.click('xpath', '//button[@aria-label="搜索"]')
wk.sleep(3)
wk.quit()
