# 实现Mock的数据生成与调用
from unittest import mock


# 伪造一个接口数据
import requests


def plus(a, b):
    return a + b
    pass


def math():
    b = plus(1, 2)
    print('math:{0}'.format(b))
    return b


# 登录专用mock函数
def login(data):
    return requests.post(url='http://39.98.138.157:5000/api/login', json=data)

# print(plus(1, 2))
# # 对指定的接口进行mock值的生成
# '''
#     mock.Mock，定义函数的返回值，无关乎函数本身内容，直接写入最终的返回结果
# '''
#
# plus = mock.Mock(return_value=2)
# c = plus(1, 2)
# print(c)
