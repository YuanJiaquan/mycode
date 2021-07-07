'''
    LoginPage:登录页，只为系统的登录业务而生成的页面对象。
'''
from selenium import webdriver




# 登录页
from Unittest.class14_pom.base_page.base_page import BasePage


class LoginPage(BasePage):
    '''
        页面对象类的模版：
            1. url
            2. 关键元素
            3. 行为
    '''
    # url
    # 假设从配置文件中获得defaults_url
    defaults_url = 'http://39.98.138.157/shopxo/index.php'
    url = defaults_url + '?s=/index/user/logininfo.html'

    # 关键元素
    username = ('xpath', '//input[@name="accounts"]')
    password = ('name', 'pwd')
    login_button = ('xpath', '//button[text()="登录"]')

    # 行为
    def login(self, user, pwd):
        # 访问登录页
        self.visit(self.url)
        # 输入账号和密码
        self.input(self.username, user)
        self.input(self.password, pwd)
        # 点击登录按钮，实现登录
        self.click(self.login_button)


# 调试
if __name__ == '__main__':
    driver = webdriver.Chrome()

    user = 'xuzhu666'
    pwd = '123456'
    lp = LoginPage(driver)
    lp.login(user, pwd)
