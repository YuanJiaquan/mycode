import json

import requests




data1={
    'username': 'admin',
    'password': '123456'
       }
data_json=json.dumps(data1)
headers={'Content-Type': 'application/json'}
print(type(data_json))
res=requests.post('http://39.98.138.157:5000/api/login',data=data_json,headers=headers)
print(res.headers)
try:
    print(res.raise_for_status())
except Exception as e:
    print(e)
print('=='*25)
print(res.text)
