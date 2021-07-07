import yaml
from appium import webdriver

f=open('../config/desired_caps.yaml', mode='r',encoding='utf-8' )
data=yaml.load(f, Loader=yaml.FullLoader)
print(data)
info={
    'platformName':data['a'],
    'platformVersion':data['b'],
    # adb devices设备名
    'deviceName':data['c'],
    # 1.aapt shell badging 安装包  aapt不是内部命令
    # 把环境变量配置一下：D:\android\Andriod_SDK\build-tools\27.0.1
    # 2.adb shell pm list packages
    # 3.adb shell dumpsys window | findstr mCurrentFocus
    'appPackage':data['appPackage1'],
    'appActivity':data['appActivity1'],
    'noReset':data['noReset1']
}
server='http://'+str(data['ip1'])+':'+str(data['port1'])+'/wd/hub'
def config():
    driver=webdriver.Remote(server,info)
    driver.implicitly_wait(10)
    return driver