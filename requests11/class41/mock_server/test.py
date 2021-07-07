from unittest import mock

from requests11.class41.mock_server.md5_apply import hashmd5, findmd5
from requests11.class41.mock_server.mock_demo import plus, math, login

# plus=mock.Mock(return_value=3)
# b = plus(2, 5)
# print(b)
# math()
#
# data={'password': '123456','username': 'admin'}
#
# login(data)

a=hashmd5('我是超级英雄')
print(a)
b=findmd5('558f8c0dae461c17c33c34f5e0652091')

