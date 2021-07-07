# import yaml
#
#
# file=open('../data/data.yaml', mode='r',  encoding='utf-8')
# data=yaml.load(stream=file,Loader=yaml.FullLoader)
# print(data)
# import requests
#
# data = {
# 'city':'1'
# }
# s={'city':'成都'}
# res=requests.get(url='http://39.98.138.157:5000/api/demo')
# print(res.status_code)
import json

import openpyxl
import requests

excel=openpyxl.load_workbook('../data/api_cases.xlsx')
sheet=excel['Sheet1']
for values in sheet.values:
    print(values)
    if type(values[0]) is int:
        try:
            url=values[1]+values[2]
            print(url)
            data1=eval(values[5])
            print(values[5])
            data={"username":"admin","password":"123456"}
            print(type(data1),type(data))
            res=requests.post(url,json=data1)
            print(res.status_code)
            print(res.json())
            assert res.json()['msg']=='success','登录失败'
            print('*'*50)
        except Exception as e:
            print(e)


