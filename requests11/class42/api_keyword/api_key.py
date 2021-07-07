'''
    这是接口关键字驱动类，用于提供自动化接口测试的关键字方法。
    主要实现常用的关键字内容，并定义好所有的参数的内容即可
    接口中的常用关键字无非就是：
        1. 各种模拟请求方法：post/get/put/delete/header/.....
        2. 设置入参的默认值时，设置的参数必须放在最后
'''
# 导包
import json

import jsonpath
import requests


class ApiKey:
    # get请求的封装：因为params可能会存在无值的情况，存放默认值None
    def do_get(self, url, params=None, **kwargs):
        # 因为请求会默认返回一个响应，所以函数定义时需要return一下
        return requests.get(url=url, params=params, **kwargs)

    # post请求的封装：data也可能存在无值的情况存,放默认值None
    def do_post(self, url, data=None, **kwargs):
        return requests.post(url=url, data=data, **kwargs)

    # 基于JsonPath获取数据的关键字：用于提取所有需要的内容
    def get_text(self, txt, key):
        # jsonpath获取数据的表达式：成功则返回list，失败则返回false
        '''
            对于json格式数据的获取，本身是存有目的性来获取的。
        '''
        try:
            txt = json.loads(txt)
            value = jsonpath.jsonpath(txt, '$..{0}'.format(key))
            if value:
                if len(value) == 1:
                    return value[0]
                return value
        except Exception as e:
            return e
        return value


if __name__ == '__main__':
    ak = ApiKey()
    data = {
        'username': 'admin',
        'password': '123456'
    }
    res = ak.do_get(url='http://39.98.138.157:5000/api/getuserinfo', timeout=0.1)
    print(res.text)
    ak.do_post(url='http://39.98.138.157:5000/api/login', json=data)
