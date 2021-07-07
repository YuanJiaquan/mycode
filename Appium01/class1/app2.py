# app常用操作  滑动 拖拽操作事件
# 应用场景：做app有些界面或者按钮需要滑动才会出来
# 滑动：
# swipe
# scroll
# drag_and_drop
# 参数信息写好
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
# 启动程序  Remote(服务器，手机配置信息)
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
driver.implicitly_wait(5)

# swipe  写法  swipe(开始x坐标，开始y坐标，结束x坐标，结束y坐标，持续时间)
# 产生惯性  持续时间越长，惯性越小
# driver.swipe(535,1610,579,635)
# driver.swipe(535,1610,579,635,3000)

# 元素滑动
# scroll(开始元素，结束元素)
# scroll滑动：从一个元素滑动到另外一个元素  也有惯性
address=driver.find_element_by_xpath('//*[@text="位置信息"]')
more=driver.find_element_by_xpath('//*[@text="更多"]')
driver.scroll(address,more)
# drag_and_drop：从一个元素滑动到另外一个元素  没有惯性
# driver.drag_and_drop(address,more)

# 可以滑动  实现滑动  选择 需不需要惯性 ，选择用坐标 还是用元素




# 等待几秒钟  等待3种方式   强制等待  直男 隐士等待  强迫症 显示等待 正常男
time.sleep(3)
# 关闭
# driver.quit()