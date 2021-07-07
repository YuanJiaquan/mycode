import json

import requests




url='http://39.98.138.157:5000/api/getproductinfo?productid=8888'


res=requests.get(url)
print(res.status_code)
print(type(res.json()))
