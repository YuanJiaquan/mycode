


from selenium import webdriver

class Options:
    def options_conf(self):
        options=webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument('start-maximized')

        # 加载缓存
        # options.add_argument(r'--user-data-dir=C:\Users\wanwan\AppData\Local\Google\Chrome\User Data')

        # 清除密码弹窗
        prefs = {}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        options.add_experimental_option("prefs", prefs)


        return options
