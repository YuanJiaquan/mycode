# 项目中基本的操作 封装在这个文件
# 输入 点击  找元素
import time

from appium import webdriver




class BaseView:
    def __init__(self,driver):
        self.driver=driver

    # 点击启动里面的哪个内容
    # 元祖解析 要加*  (By.ID,'android:id/button2')
    # 元素定位
    def loctor(self,loc):
       return self.driver.find_element(*loc)

    # 输入  找到元素 在进行输入
    def on_input(self,loc,txt):
        self.loctor(loc).send_keys(txt)
        # try:
        #     log.info('定位{}元素，输入{}'.format(loc,txt))
        #     self.loctor(loc).send_keys(txt)
        # except Exception as e:
        #     log.error('输入失败')

    # 点击 找到元素 在进行点击
    def on_click(self,loc):
        self.loctor(loc).click()

    # 等待
    def wait(self):
        time.sleep(3)

    # 关闭
    def close(self):
        self.driver.quit()

    # 获得窗口大小
    def get_window_size(self):
        return self.driver.get_window_size()

    # 滑动  x,y  x[0]*90
    def swipe(self,start_x,start_y,end_x,end_y,t):
        return self.driver.swipe(start_x,start_y,end_x,end_y,t)
