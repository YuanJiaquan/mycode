# 课后作业：
# 1. 将关键字驱动类实现，包含健壮性需要考虑在内
# 2. 将浏览器配置的options类，与关键字驱动类实现联动结合。来实现自动化
# 3. 将日志配置类Logging，与关键字这一套进行结合，将所有的输入定位为日志形式
# 作业核心思路：
# 类与函数的定义。
from time import sleep


from 配置.webkey import WebKeys

wk = WebKeys('Chrome')
wk.open('http://39.98.138.157/shopxo/')
# data={'name':'link text', 'value':'登录'}

wk.click(name='link text',value='登录')


wk.input(name='name', value='accounts',txt= 'xuzhu666')

wk.input(name='name', value='pwd', txt='123456')

wk.click(name='xpath',value= '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')

sleep(3)

wk.quit()