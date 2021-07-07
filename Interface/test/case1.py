import json
import unittest
from ddt import ddt,file_data
from Interface.key.key_api import ApiKey

@ddt
class mytest(unittest.TestCase):
    def setUp(self) -> None:
        self.defulturl='http://39.98.138.157:5000/'

    @file_data('../data/data.yaml')
    def test01(self,**kwargs):
        url=self.defulturl+kwargs['url']
        print(url)
        ap=ApiKey()
        ap.sw123(123)
        print(kwargs)
        data={'password':kwargs['password'],'username':kwargs['username']}
        res=ap.do_post(url=url,json=data)
        print(res.json())

    @file_data('../data/data.yaml')
    def test02(self,**kwargs):
        print(kwargs['url'])


if __name__ == '__main__':
    unittest.main()





