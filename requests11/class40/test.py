import requests
import json

data = {
    "username": "admin",
    "password": "123456"
}

print(data)
print(type(data))

requests.post(url='http://www.baidu.com')