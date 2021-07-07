import requests

# 接口关联案例
session = requests.session()
print(session.cookies)
url = 'http://39.98.138.157:5000/api/login'
data = {
    'username': 'admin',
    'password': '123456'
}
res = requests.post(url=url, json=data)

url = 'http://39.98.138.157:5000/api/getuserinfo'
headers = {
    'token': res.json()['token']
    # 'token': 'asdjaldannzxc,'
}
res = requests.get(url=url, headers=headers)
print(res.text)
# print(session.cookies)

# 基于session来实现接口关联的方案:session的创建意味着，基于这个session所产生的相关session信息，都会被保存
# session = requests.session()
# session.get()
# session.post()
