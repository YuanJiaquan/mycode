from 配置.log import log
import logging
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction


class baseClass():

    def __init__(self,driver):

        self.driver=driver

    def locator(self,name,value):
        return self.driver.find_element(name,value)

    def click(self,name,value):
        self.locator(name,value).click()

    def check_cancel(self,**kwargs):
        print('# 点击取消')
        try:
            self.driver.find_element_by_id(kwargs['id']).click()
            # 把操作记录在日志里面
        except Exception as e:
            print('没有取消按钮')

    def check_skip(self,**kwargs):
        print('# 点击跳过')
        try:
            self.driver.find_element_by_xpath(kwargs['xpath']).click()
            # 把操作记录在日志里面
        except Exception as e:
            print('没有跳过按钮')

    def input(self,txt,name,value):
        log().info('定位{}元素，元素值为{},并在此处输入内容{}'.format(name,value,txt))
        self.locator(name,value).send_keys(txt)




    def checkinfo(self,name,value):
        log().info('执行断言')
        try:
            text=self.locator(name,value).text
            # text=el.getAttribute('value')
            print(text)
            assert text=='确定1','登录失败'
        except Exception as e:
            print(e)

    def getsize(self):
        return  self.driver.get_window_size()

    def swipe_left(self):
        pass

    def swipe_right(self):
        pass

    def zoom_in(self):
        x=self.getsize()['width']
        y=self.getsize()['height']
        action1 = TouchAction(self.driver)
        action1.press(x=x * 0.2, y=y * 0.2).wait(1000).move_to(x=x * 0.4, y=y * 0.6).wait(1000).release()
        action2 = TouchAction(self.driver)
        action2.press(x=x * 0.8, y=y * 0.8).wait(1000).move_to(x=x * 0.5, y=y * 0.5).wait(1000).release()
        print('执行缩小操作')
        zoom = MultiAction(self.driver)
        zoom.add(action1, action2)
        zoom.perform()

    def zoom_out(self):
        pass


