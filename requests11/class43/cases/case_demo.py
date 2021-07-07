import unittest
from class43.conf import read_ini
from ddt import ddt, file_data
from class42.api_keyword.api_key import ApiKey

'''
    接口测试的操作执行核心：
        1. 准备数据
        2. 发送请求
        3. 判断响应
'''


@ddt
class CaseDemo(unittest.TestCase):
    # 关联数据赋值行为
    def assignment(self, kwargs):
        for key, value in kwargs.items():
            # 基于数据内容的格式来进行判断该用何种处理方式
            if type(value) is dict:
                self.assignment(value)
            else:
                if value:
                    pass
                else:
                    kwargs[key] = getattr(self, key)
        return kwargs
    # 定义接口中关联的全局变量
    @classmethod
    def setUpClass(cls) -> None:
        cls.ak = ApiKey()
        cls.url = read_ini.ReadIni('../conf/config.ini', 'TEST_SERVER', 'url')
        cls.token = None
        cls.userid = None
        cls.openid = None
        cls.cartid = None

    # 测试用例的定义:Login接口的测试用例
    @file_data('../data/user.yaml')
    def test_1(self, path, data):
        url = self.url + path
        res = self.ak.do_post(url=url, json=data)
        # 赋值全局变量
        token = self.ak.get_text(res.text, 'token')
        if token:
            CaseDemo.token = token

    # getuserinfo接口的测试用例
    @file_data('../data/userinfo.yaml')
    def test_2(self, path, headers):
        url = self.url + path
        headers['token'] = self.token
        res = self.ak.do_get(url=url, headers=headers)
        userid = self.ak.get_text(res.text, 'userid')
        openid = self.ak.get_text(res.text, 'openid')
        if userid:
            CaseDemo.userid = userid
        if openid:
            CaseDemo.openid = openid

    # addcart接口的用例
    @file_data('../data/addcart.yaml')
    def test_3(self, path, headers, data):
        url = self.url + path
        headers['token'] = self.token
        data['openid'] = self.openid
        data['userid'] = self.userid
        res = self.ak.do_post(url=url, headers=headers, json=data)
        print(res.text)
        cartid = self.ak.get_text(res.text, 'cartid')
        if cartid:
            CaseDemo.cartid = cartid

    # createorder接口的用例
    @file_data('../data/order.yaml')
    def test_4(self, path, **kwargs):
        url = self.url + path
        # headers['token'] = self.token
        # data['openid'] = self.openid
        # data['userid'] = self.userid
        # data['cartid'] = self.cartid
        value = self.assignment(kwargs)
        res = self.ak.do_post(url=url, headers=value['headers'], json=value['data'])
        print(res.text)


if __name__ == '__main__':
    unittest.main()
