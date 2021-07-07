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
    'appActivity':'com.android.settings.ChooseLockPattern',
    # 不重置
    'noReset':False
}
# 启动程序  Remote(服务器，手机配置信息)
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
driver.implicitly_wait(5)

# 移动
TouchAction(driver).press(x=179,y=625).wait(1000)\
    .move_to(x=894,y=623).wait(1000).move_to(x=894,y=1337)\
    .release().perform()


# 指针位置：开发者选项 指针位置
# 作业：实现考研帮的登录  账号  密码 qwerty2664  qwerty123
