# 考研班实现登录
import time

from appium import webdriver

# 一个个优化
# 配置信息。经常要变化的参数  配置文件中。yaml

info={
    'platformName':'Android',
    'platformVersion':'5.1.1',
    # adb devices设备名
    'deviceName':'1',
    # 1.aapt shell badging 安装包  aapt不是内部命令
    # 把环境变量配置一下：D:\android\Andriod_SDK\build-tools\27.0.1
    # 2.adb shell pm list packages
    # 3.adb shell dumpsys window | findstr mCurrentFocus
    'appPackage':'com.tal.kaoyan',
    'appActivity':'com.tal.kaoyan.ui.activity.SplashActivity',
    'noReset':False
}
# Remote服务器地址  配置信息
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)


# 封装起来 函数
def check_cancel():
    print('# 点击取消')
    try:
        cancel=driver.find_element_by_id('android:id/button2')
        cancel.click()
        # 把操作记录在日志里面
    except Exception as e:
        print('没有取消按钮')

def check_skip():
    print('# 点击跳过')
    try:
        skip=driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
        skip.click()
    except Exception as e:
        print('没有跳过按钮')


def login():
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    # 找到输入框输入用户名
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('qwerty2664')
    # 找到密码框输入密码
    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('qwerty123')
    # 找到登录按钮进行点击
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()


check_cancel()

# swipe(开始x坐标，开始y坐标，结束x坐标，结束y坐标,持续时间)
# driver.swipe(834,954,224,1050)
# 智能获取
# 1.屏幕大小
width=driver.get_window_size()['width']
height=driver.get_window_size()['height']

# check_skip()
# 等待
time.sleep(3)
login()
time.sleep(3)
driver.quit()

# 实现自动化的效果
# 项目结构

