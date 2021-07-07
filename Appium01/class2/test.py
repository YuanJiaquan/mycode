from time import sleep

from appium import webdriver
# 配置信息  这些参数会要经常变换 配置文件 ini config yaml
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from Appium01.myframe.BaseView.BaseView import baseClass

info={
    'platformName':'Android',
    'platformVersion':'5.1.1',
    'deviceName':'2',
    'appPackage':'com.baidu.BaiduMap',
    'appActivity':'com.baidu.baidumaps.MapsActivity',
    'noReset':True
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
# 等待页面加载出来
driver.implicitly_wait(10)

# 1.获取屏幕尺寸
# x=driver.get_window_size()['width']
# y=driver.get_window_size()['height']
#
# action1=TouchAction(driver)
# action1.press(x=0.2*x,y=0.2*y).wait(1000).move_to(x=0.5*x,y=0.5*y).wait(1000).release()
# # action1.press(x=x*0.2,y=y*0.2).wait(1000).move_to(x=x*0.4,y=y*0.6).wait(1000).release()
# action2=TouchAction(driver)
# action2.press(x=0.9*x,y=0.9*y).wait(1000).move_to(x=0.6*x,y=0.6*y).wait(1000).release()
# zoom=MultiAction(driver)
# zoom.add(action1,action2)
# zoom.perform()

bc=baseClass(driver)
for i in  range(5):
    bc.zoom_in()
    sleep(3)