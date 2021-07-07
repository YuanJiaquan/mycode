from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

appinfo={
    "platformName":"Android",
    "platformVersion":"5.1.1",
    "deviceName":"1",
    "appPackage":"com.wondershare.drfone",
    "appActivity":"com.wondershare.drfone.ui.activity.WelcomeActivity",
    "noRest":True,
    "unicodeKeyboard":True,
    "resetKeyboard":True,
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', appinfo)
driver.implicitly_wait(5)

print('点击backup按钮')
driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()
print('点击backup完成')
WebDriverWait(driver,20).until(lambda x:x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))

print('点击next按钮')
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()

print('获取contexts完成')
contexts=driver.contexts
print(contexts)

driver.implicitly_wait(10)
driver.switch_to.context('NATIVE_APP')
# driver.switch_to.context('WEBVIEW_com.wondershare.drfone')
print('已经切换到内嵌网页7')

driver.find_element_by_id('email').send_keys('123@wondershare.cn')

print('页面操作完成，准备开始跳出h5页面8')
#切换context 点击返回
driver.switch_to.context(contexts[0])
# driver.switch_to.context('NATIVE_APP')
print('跳出h5，返回app，完成 9')

# 用这个案例，需要每次手动点一下