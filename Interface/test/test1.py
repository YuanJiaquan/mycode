import requests

data = {
'city':'1'
}
s={"username":"admin","password":"123456"}
res=requests.post(url='http://39.98.138.157:5000/api/login',json=s)
print(res.json())