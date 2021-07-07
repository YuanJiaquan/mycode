import time

from appium import webdriver
info={
    # 操作平台  操作 安卓 苹果  Android不区分大小写，不能写错
    'platformName':'Android',
    # 版本号  设置 关于平板电脑 版本号
    'platformVersion':'5.1.1',
    # 设备名 adb devices 检测设备名  可以随意写 不要空  不要中文
    'deviceName':'127.0.0.1:62001',
    # 包名
    'appPackage':'com.android.settings',
    # 应用名
    'appActivity':'com.android.settings.Settings',
    # 不重置
    'noReset':False
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
driver.implicitly_wait(10)
x=driver.get_window_size()['width']
y=driver.get_window_size()['height']
print(x,y)
driver.swipe(0.2*x,0.8*y,0.2*x,0.2*y)

address=driver.find_element_by_xpath('//*[@text="位置信息"]')
more=driver.find_element_by_xpath('//*[@text="关于平板电脑"]')
driver.scroll(address,more)
