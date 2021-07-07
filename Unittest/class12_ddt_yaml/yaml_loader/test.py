import openpyxl
import yaml

# file = open('H:/python/yaml1/Unittest/data/data.yaml', 'r', encoding='utf-8')
# # 读取yaml文件中的内容
# data = yaml.load(stream=file, Loader=yaml.FullLoader)
# print(data)

excel=openpyxl.load_workbook('H:/python/yaml1/Unittest/data/data.xlsx')
sheet=excel['Sheet1']
for values in sheet.values:
    if type(values[0]) is int:
        data={}
        data['name'] = values[2]
        data['value'] = values[3]
        data['txt'] = values[4]
        for  key in list(data.keys()):
            if data[key] is None:
                del data[key]
        print(values)