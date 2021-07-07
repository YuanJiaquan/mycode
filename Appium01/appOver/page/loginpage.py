# 封装登录的内容
from selenium.webdriver.common.by import By

from common.common_fun import Common


# 单继承  爷爷--父亲继承了基因 --儿子的基因
from common.desired_caps import appium_desired


class LoginView(Common):
    # 登录元素
    # 用户名
    # 密码
    # 按钮
    username_type=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_type=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
    loginBtn=(By.ID,'com.tal.kaoyan:id/login_login_btn')

    myself=(By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    userinfo=(By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

    # 设置
    set=(By.ID,'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    out=(By.ID,'com.tal.kaoyan:id/setting_logout_text')
    # 登录的流程 输入用户名  输入密码  点击登录   常用方法已经封装
    def login(self,username,password):
        self.check_cancel()
        self.check_skip()

        self.on_input(self.username_type,username)
        self.on_input(self.password_type,password)
        self.on_click(self.loginBtn)

    # def check_alter(self):
    #     print('检查弹窗')
    #     try:
    #


    # 检测登录状态的方法  可能会弹出一个弹窗  弹窗也要定位到
    def login_status(self):
        try:
            self.on_click(self.myself)
            self.loctor(self.userinfo)
        except Exception as  e:
            print('登录失败')
            return False
        else:
            print('登录成功')
            # 退出的方法
            self.loginOut()
            return True

    # 退出登录
    def loginOut(self):
        self.on_click(self.set)
        self.on_click(self.out)


if __name__ == '__main__':
    driver = appium_desired()
    l=LoginView(driver)
    l.login('qwerty2664','qwerty123')

# 登录的方法写完后，测试