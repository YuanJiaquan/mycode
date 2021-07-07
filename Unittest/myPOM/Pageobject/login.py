from Unittest.myPOM.Basepage.Basepage01 import BasePage01


class Login(BasePage01):

    default_url='http://39.98.138.157/shopxo/index.php'
    url=default_url+'?s=/index/user/logininfo.html'

    username = ('xpath', '//input[@name="accounts"]')
    password = ('name', 'pwd')
    login_button = ('xpath', '//button[text()="登录"]')


    def login(self,name,pwd):
        self.visit(self.url)
        self.input(self.username,name)
        self.input(self.password,pwd)
        self.click(self.login_button)

