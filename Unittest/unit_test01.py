import unittest
from time import sleep
import ddt
import yaml

from 配置.excel_webkey import WebKeys
from 配置.webkey import WebKeys1
from ddt import ddt,data,file_data,unpack

@ddt
class Unit_test001(unittest.TestCase):
    # file=open('./data/test_data.yaml',mode='r', encoding='utf-8')
    # data=yaml.load(stream=file, Loader=yaml.FullLoader)

    # @ddt.file_data('./data/test_data.yaml')
    # @unittest.skip('nihaop')
    # def test_01(self,**kwargs):
    #     self.wk = WebKeys1('Chrome')
    #     self.wk.open(kwargs['url'])
    #     self.wk.input(**kwargs['input'])
    #     self.wk.click(**kwargs['click'])
    #     self.wk.sleep(3)

    @data((1,2),(3,5))
    @unpack
    def test04(self,x,y):
        print(x+y)
    @unittest.skip('无理由跳过')
    @file_data('../Unittest/data/test_data.yaml')
    def test05(self,**kwargs):
        self.wk = WebKeys1('Chrome')
        self.wk.open(kwargs['url'])
        self.wk.input(**kwargs['input'])

        print(kwargs)
    def test06(self):
        print('06')

    @file_data('../Unittest/data/data.yaml')
    @unpack
    def test04(self, **kwargs):
        if kwargs['w'] == 'open_browser':
            self.wk = WebKeys('Chrome')
        elif kwargs['w'] == 'assert_text':
            pass
        else:
            a1 = kwargs['w']
            print(a1)
            self.kw.a1(**kwargs)

if __name__ == '__main__':
    unittest.main()