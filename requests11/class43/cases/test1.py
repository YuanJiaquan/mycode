import requests

url = 'http://39.98.138.157:5000/api/login'

data={"password": "123456","username": "admin"}
session=requests.session()
res=requests.post(url,json=data)

print('*'*25)
print(session)

j=res.json()

print(j)
token='23657DGYUSGD126731638712GE18271H'
headers={'token':token}
url1='http://39.98.138.157:5000/api/getuserinfo'
res2=requests.get(url1,headers=headers)
print(res2.json())
print('-'*25)

