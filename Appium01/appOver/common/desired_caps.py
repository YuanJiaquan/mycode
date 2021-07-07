# 先拿到配置
# 启动的配置信息
# 文件的值  pip install pyyaml

import yaml
from appium import webdriver

from log.mylog import test_log

log=test_log()
def appium_desired():
    # 拿yaml文件 ./  还是../
    with open('../config/desired_caps.yaml')as f:
        # 拿yaml文件的数据
        data=yaml.load(f,yaml.FullLoader)
        print(data)

    # 拿到数据之后，放在配置参数里面  Android  字典怎么取值
    # 'platformName':'Android1',
    info={}
    info['platformName']=data['a']
    info['platformVersion']=data['b']
    info['deviceName']=data['c']
    info['appPackage']=data['appPackage1']
    info['appActivity']=data['appActivity1']
    info['noReset']=data['noReset1']

    # driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
    log.info('启动app')
    driver=webdriver.Remote('http://'+data['ip1']+':'+str(data['port1'])+'/wd/hub',info)
    driver.implicitly_wait(8)
    return driver

# 启动了一个程序  登录程序  跳过，取消常用操作