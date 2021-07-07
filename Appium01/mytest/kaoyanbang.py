from time import sleep

from appium import webdriver



info={
    # 操作平台  操作 安卓 苹果  Android不区分大小写，不能写错
    'platformName':'Android',
    # 版本号  设置 关于平板电脑 版本号
    'platformVersion':'5.1.1',
    # 设备名 adb devices 检测设备名  可以随意写 不要空  不要中文
    'deviceName':'127.0.0.1:62001',
    # 包名
    'appPackage':'com.tal.kaoyan',
    # 应用名
    'appActivity':'com.tal.kaoyan.ui.activity.SplashActivity',
    # 不重置
    'noReset':False
}

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
driver.implicitly_wait(5)
driver.find_element_by_id('android:id/button2').click()
sleep(3)
skip=driver.find_element('xpath','//*[@resource-id="com.tal.kaoyan:id/tv_skip"]').click()
el1=driver.find_element('xpath','//*[@text="请输入用户名"]')
el2=driver.find_element('xpath','//*[@resource-id="com.tal.kaoyan:id/login_password_edittext"]')
el1.send_keys('jiaquan0729')
el2.send_keys('772878309quan')
driver.find_element('xpath','//*[@text="登录"]').click()
driver.get_window_size()











# sleep(3)
# driver.quit()

