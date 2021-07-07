import unittest
from unittest import mock, TestCase
import requests

from requests11.class41.mock_server import mock_demo


class Demo(TestCase):
    # 常规形态下的mock实现
    # def test_1(self):
    #     mock_demo.plus = mock.Mock(return_value=5)
    #     c = mock_demo.math()
    #     print(c)

    # 基于装饰器的形态来实现的mock：定义哪个接口需要进行mock
    @mock.patch('mock_demo.login')
    def test_2(self, mock_login):
        # 已经完成了Mock数据的生成：mock的操作相当于自主定义生成测试数据，快速提供至测试行为之中
        a = mock_login.return_value = {'password': '123456',
                                       'username': 'admin'}
        # a = mock_demo.login()
        res = requests.post(url='http://39.98.138.157:5000/api/login', json=a)
        print(res.text)

    # mock实现形式3：如果要实现多次调用，每次有不同的值
    @mock.patch.object(mock_demo, 'plus')
    def test_3(self, mock_plus):
        mock_plus.side_effect = [
            'plus1',
            'plus2',
            'plus3'
        ]
        for i in range(0, 3):
            mock_demo.math()


if __name__ == '__main__':
    unittest.main()
