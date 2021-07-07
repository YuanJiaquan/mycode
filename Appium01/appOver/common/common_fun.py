# 运用到pom思想  页面元素分离出来
# 页面元素经验要去变化  页面元素可提取出来
# 公共
from selenium.webdriver.common.by import By
from baseView.baseView import BaseView
# 继承
from common.desired_caps import appium_desired

# 类 对象  变量 方法

class Common(BaseView):
    # 取消的元素
    cancel=(By.ID,'android:id/button2')
    skip=(By.ID,'com.tal.kaoyan:id/tv_skip')

    # 封装起来 函数  找元素 ，点击，输入操作 web自动化  基本的操作  封装关键字驱动
    # 使用
    def check_cancel(self):
        print('# 点击取消')
        try:
            self.on_click(self.cancel)
            # 把操作记录在日志里面
        except Exception as e:
            print('没有取消按钮')

    def check_skip(self):
        print('# 点击跳过')
        try:
           self.on_click(self.skip)
        except Exception as e:
            print('没有跳过按钮')

    # 获得窗口大小
    def get_size(self):
        x=self.get_window_size()['x']
        y=self.get_window_size()['y']
        return x,y

    # 滑动
    def swipeLeft(self):
        l=self.get_size()
        x1=l[0]*0.9
        y1 = l[1] * 0.5
        x2=l[0]*0.2
        self.swipe(x1,y1,x2,y1,1000)



    # 滑动
if __name__ == '__main__':
    driver=appium_desired()
    com=Common(driver)
    com.check_cancel()
    com.check_skip()

# 登录的操作
# 登录页面  支付页面  下单页面  购物页面
# pom


