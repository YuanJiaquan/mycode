from time import sleep

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
class WebKeys:
    # driver=webdriver.Chrome(options=Options().options_conf())

    def __init__(self, type_):
        self.driver = getattr(webdriver,type_)(options=Options().options_conf())
        # self.driver = getattr(webdriver, type_)()
        self.driver.implicitly_wait(10)

        pass

    def open(self,**kwargs):
        log.info('访问URL{}'.format(kwargs['txt']))
        self.driver.get(kwargs['txt'])



    def locator(self, **kwargs):
        log.info('正在定位{}元素，元素值为{}'.format(kwargs['name'], kwargs['value']))
        return self.driver.find_element(kwargs['name'], kwargs['value'])


    def click(self, **kwargs):
        self.locator(**kwargs).click()


    def input(self, **kwargs):
        el = self.locator(**kwargs)
        el.clear()
        el.send_keys(kwargs['txt'])

    def assert_text(self,**kwargs):
        el=self.locator(**kwargs)
        try:
            assert el.text == kwargs['txt']
            return True
        except:
            return False

    def sleep(self,**kwargs):
        log.info('等待{}秒'.format(kwargs['txt']))
        sleep(kwargs['txt'])

    def quit(self):
        self.driver.quit()




