# python代码实现启动程序定位

# 安装 pip.exe install appium-python-client setting里面安装
import time

from appium import webdriver
# appium继承了selenium


# 参数信息写好
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
driver=webdriver.Remote('http://0.0.0.0:4723/wd/hub',info)
driver.implicitly_wait(5)
# 元素定位  常用id class xpath
# 点击搜索  id
# driver.find_element_by_id('com.android.settings:id/search').click()
# 点击搜索 class_name
# driver.find_element_by_class_name('android.widget.TextView').click()
# 点击搜索 xpath
# driver.find_element_by_xpath('//*[@content-desc="搜索"]').click()
#  accessibility
# driver.find_element_by_accessibility_id('搜索').click()
# uiautomator  id class text
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.settings:id/search")').click()

# 组合在一起  实现搜索 qiushui 返回
# 点击搜索
# driver.find_element_by_id('com.android.settings:id/search').click()
# # 选择搜索框
# driver.find_element_by_class_name('android.widget.EditText').send_keys('qiushui')
# # 返回
# driver.find_element_by_xpath('//*[@content-desc="收起"]').click()


# 一次性定位到很多值
# id 唯一 身份证号  class_name相当于名字  名字重名
titles=driver.find_elements_by_class_name('android.widget.TextView')
# 打印有多少个值
print(len(titles))
# 内容文本值全部打印出来
for i in titles:
    print(i.text)
# 下标
titles[4].click()


# 等待几秒钟  等待3种方式   强制等待  直男 隐士等待  强迫症 显示等待 正常男
time.sleep(8)
# 关闭
driver.quit()