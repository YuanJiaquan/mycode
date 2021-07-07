# 多点触控multiAction,是touchAction的一个补充模块。更高级
# touchAction高级手势，一个手指移动
# 两个手指一起移动，多个点移动
# 百度地图 放大缩小
# touchAction步骤：
# 1.创建touchAction对象
# 2.通过对象调用我们想要执行的操作
# 3.通过perform()执行

# multiAction
# 步骤：
# 1.创建两个手指 创建2个touchAction对象
# 2.创建mulitAction()对象
# 3.把2个touchAction对象，添加进mulitAction()对象
# 4.通过perform()执行
import time

from appium import webdriver
# 配置信息  这些参数会要经常变换 配置文件 ini config yaml
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

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
driver.implicitly_wait(5)

# 1.获取屏幕尺寸
x=driver.get_window_size()['width']
y=driver.get_window_size()['height']

# x1980 *0.6

# 2.缩小地图  放大地图
# 一个手指头
def zoo():
    action1=TouchAction(driver)
    action1.press(x=x*0.2,y=y*0.2).wait(1000).move_to(x=x*0.4,y=y*0.6).wait(1000).release()
    action2=TouchAction(driver)
    action2.press(x=x*0.8,y=y*0.8).wait(1000).move_to(x=x*0.5,y=y*0.5).wait(1000).release()
    print('执行缩小操作')
    zoom=MultiAction(driver)
    zoom.add(action1,action2)
    zoom.perform()

if __name__ == '__main__':
    for i in range(3):
        zoo()

# 布置两个作业：
# 1.滑动  向左滑动  向右滑动  向上滑动  向下滑动
# 2.放大缩小  缩小  放大

# 混合apph5的定位
# app分为3类  原生的(JAVA)  混合的(JAVA+H5)  H5(HTML+CSS+JAVASCTPT)
# 怎么去分辨  边界
# 不好去定位 content切换到webview模式
# 如果想做h5的元素操作
# 环境准备一下
# 1.下载uc-devtools工具之后
# 2.浏览器的驱动 配套 下载配套的驱动
# 放在appium安装包下  C:\Users\76597\AppData\Local\Programs\Appium\resources\app\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win
# 把旧版本保存下来，把新版本放进去
# 3.在d盘新建一个目录，把chome驱动放进去就行了
