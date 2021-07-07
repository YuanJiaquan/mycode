# 高级手势 TouchAction
# 基本的手势组合在一起变成高级手势  基本的手势  移动，按下，抬起，轻敲
# 步骤：
'''
1.创建一个touchAction对象
2.对象调用我们想要做的操作
3.通过perform()
'''

import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

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
# 启动程序  Remote(服务器，手机配置信息)
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
driver.implicitly_wait(5)

'''
1.创建一个touchAction对象
2.对象调用我们想要做的操作
3.通过perform()
'''
# 基本事件  轻敲(元素),坐标
# 模拟对蓝牙进行轻敲
# bluetooth=driver.find_element_by_xpath('//*[@text="蓝牙"]')
# action=TouchAction(driver)
# action.tap(bluetooth)
# action.perform()

# action=TouchAction(driver)
# action.tap(x=643,y=464)
# action.perform()
#
# TouchAction(driver).tap(x=643,y=464).perform()

# 按下和抬起  .press()按下  release抬起
# TouchAction(driver).press(x=643,y=464).release().perform()

# 等待
# TouchAction(driver).press(x=643,y=464).wait(1000).release().perform()

# 移动
