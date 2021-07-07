from selenium import webdriver
from 配置.Chrome_options import Options
from 配置.log import log
def browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver
log=log()
class WebKeys1:
    # driver=webdriver.Chrome(options=Options().options_conf())

    def __init__(self, type_):
        self.driver = getattr(webdriver,type_)(options=Options().options_conf())
        # self.driver = getattr(webdriver, type_)()
        self.driver.implicitly_wait(10)

        pass

    def open(self,url):
        log.info('访问URL{}'.format(url))
        self.driver.get(url)



    def locator(self, **kwargs):
        log.info('正在定位{}元素，元素值为{}'.format(kwargs['name'], kwargs['value']))
        return self.driver.find_element(kwargs['name'], kwargs['value'])


    def click(self, **kwargs):
        self.locator(**kwargs).click()


    def input(self, **kwargs):
        el = self.locator(**kwargs)
        el.clear()
        el.send_keys(kwargs['txt'])

    def quit(self):
        self.driver.quit()




