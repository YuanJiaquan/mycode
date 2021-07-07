'''
    关键字驱动类：
        Selenium就是一个大商场。按照自己的需要去买需要的东西。因为只有自己需要的东西才会有价值。
        所以将Selenium中我们需要的内容进行提取，带回家，变成对自己有价值的内容。
        关键字驱动就是很多人口中所谓的Selenium的二次封装。
        常用的Selenium操作行为：
            1. 元素定位
            2. 输入
            3. 点击
            4. 关闭
            5. 等待
            6. 切换句柄
            7. 访问url
            8. 创建webdriver对象
            。。。。。。
        在封装Selenium的时候请像个直男，只要自己要的。
        在初期封装完成的关键字驱动类，可以依照自己最初的定义去封装，
        如果发现有内容无法基于现有类满足，就继续添加新的关键字即可。
'''
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver

# 要满足创建任意一个浏览器对象的需求。Chrome,chrome
# from class06_options_webui.chrome_options import Options


# 不同的driver初始化形式，自己挑喜欢的
def open_browser(type_):
    # 基于反射的形态来简化代码
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver
    # try:
    #     if type_ == 'Chrome':
    #         return webdriver.Chrome(options=Options().conf_options())
    #     else:
    #         return getattr(webdriver, type_)()
    # except:
    #     return webdriver.Chrome()


# 在后续的自动化中通过调用这个类，来实现Selenium操作:逻辑代码
class WebKey:
    # 定义常规的测试操作行为
    # 创建一个临时driver对象，便于代码的编写。
    # driver = webdriver.Chrome()
    # 构造函数：用于初始化self.driver对象。要考虑到driver对象可能是任意的一种浏览器。
    def __init__(self, type_):
        self.driver = open_browser(type_)
        # 隐式等待
        self.driver.implicitly_wait(10)

    # 访问url
    def visit(self, url):
        self.driver.get(url)

    # 关闭释放资源
    def quit(self):
        self.driver.quit()

    # 元素定位:目的是为了通过一个方法实现所有的元素定位。
    # 如果不return，就无法获得你定位的元素对象，在后续执行输入这一类操作的时候就会报错。
    def locator(self, name, value):
        return self.driver.find_element(name, value)

    # 对于元素定位，如果有复数，该怎么办。 复数的定位很少用到。只有在特定场景下才会有。所以可以先不管它。
    # 复数定位。
    # def locator_s(self):
    #     pass

    # 输入
    def input(self, name, value, txt):
        self.locator(name, value).send_keys(txt)

    # 点击
    def click(self, name, value):
        self.locator(name, value).click()

    # 强制等待
    def sleep(self, time_):
        sleep(time_)

    # 显示等待
    def wait(self, name, value):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locator(name, value), message='等待失败')
    # 隐式等待：不需要封装，一般而言隐式是配置，是固定的等待时间。
    # 句柄切换，包含关闭原页面
    # 句柄切换，不包含原页面
