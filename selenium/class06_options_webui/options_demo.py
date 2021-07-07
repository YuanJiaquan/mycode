'''
    ChromeOptions配置(专门用于在启动driver对象前，对其进行一系列的配置)：
    options所有的配置参数，其实应该没有谁记得住。所以一般在应用的时候，通过百度去查看这个指令用什么函数添加
    特定的指令可以通过百度来获取，辨别指令有效的方式：
        1. 自行copy，再运行，查看是否生效。（推荐）
        2. 针对一些老的指令，现有的版本可能失效，如何评估是老的指令呢？ 通过driver = webdriver.Chrome(options=options)来辨别
            老的版本参数是chrome_options，新版本是options
    配置项：
        1. 窗体最大化，默认的driver函数运行时会有延时，以及部分页面在driver默认大小
            启动的时候会是以移动端的形式来显示页面内容。
        2. 去掉警告条
        3. 让driver对象加载本地缓存：不推荐大家使用，因为很不友好。现在有了提速之后，推荐使用
            使用步骤：
                1. 输入chrome://version，查看个人资料路径
                2. 通过参数--user-data-dir=将资料路径加载进driver对象
                3. 在调用本地缓存之前，一定要关闭所有的浏览器。
                4. 在03期的时候，应用selenium是3.x的版本。会有一个问题：因为要加载
                    本地缓存到浏览器，所以启动浏览器的速度会特别特别特别慢。需要通过
                    手动输入一个url去进行访问，从而实现加载的提速
                5. 如果说解决了登录的问题，基本解决了90%的验证码问题。
        4. 无头模式：--headless
            1. 默认启动的driver对象，是一个可视化浏览器，所有操作都基于可视化的形态来实现，会速度慢一些，资源耗费高一些。
            2. 无头模式也就意味着启动一个看不见的浏览器。所有的操作都是基于后台进程完成的，不会在界面显示。
            3. 断言在无头下会报错。这个问题是个新的问题，还有在集成jenkins时，有部分代码因为无头会报错，取消无头就正常。
            4. 多浏览器并发运行时，无头可以极大地降低使用资源，提升效率。
        5. 添加配置项，去掉密码管理弹窗。
            1. 通过添加一个字典参数来配置
        6. 隐身模式：没啥用，纯粹是为了私密
        7. 指定窗口大小：做尺寸适配的设置
        8. 在指定位置打开浏览器：看着会舒服点

'''

from time import sleep

from selenium import webdriver

# # 配置ChromeOptions
# options = webdriver.ChromeOptions()
# # 默认启动的driver窗体最大化
# # options.add_argument('start-maximized')
# # 去掉提示正在执行自动化的警告条：没啥用，仅限于强迫症患者以及部分特别的系统。
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# # 这个现在已经用不了了，这是老版本去掉警告条的方式
# # options.add_argument('disable-infobars')
# # 添加本地缓存
# options.add_argument(r'--user-data-dir=C:\Users\15414\AppData\Local\Google\Chrome\User Data')
# # 添加无头指令：有斟酌地进行使用。
# # options.add_argument('--headless')
# # 添加去掉密码弹窗管理
# prefs = {}
# prefs["credentials_enable_service"] = False
# prefs["profile.password_manager_enabled"] = False
# options.add_experimental_option("prefs", prefs)
# # 隐身模式
# options.add_argument('incognito')
# # 指定窗口大小的指令
# # options.add_argument('window-size=2000,4000')
# # 默认浏览器启动的坐标位置
# options.add_argument('window-position=200,400')

# 配置参数加入driver对象中
from class06_options_webui.chrome_options import Options

driver = webdriver.Chrome(options=Options().conf_options())
driver.implicitly_wait(10)
# sleep(3)
# driver.maximize_window()
driver.get('http://www.baidu.com')
