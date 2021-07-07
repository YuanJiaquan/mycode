import unittest
from ddt import ddt, file_data

from class42.api_keyword.api_key import ApiKey


@ddt
class ApiCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ak = ApiKey()

    # def setUp(self) -> None:
    #     self.ak = ApiKey()
    @file_data('../data/user.yaml')
    def test_1(self, user, msg):
        # ak = ApiKey()
        url = 'http://39.98.138.157:5000/api/login'
        data = {
            'username': user['username'],
            'password': user['password']
        }
        res = self.ak.do_post(url=url, json=data)
        print(res.text)
        # 获取响应中的结果，用于校验是否成功
        msg1 = self.ak.get_text(res.text, 'msg')
        print(msg1)
        self.assertEqual(msg1, msg, msg='异常')


if __name__ == '__main__':
    unittest.main()
