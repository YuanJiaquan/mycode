import yaml

'''
    yaml读取文件与常规文件不同，通过open形成file格式的内容，基于yaml库来实现内容的识别和读取
'''
file = open('./data/data_dict.yaml', 'r', encoding='utf-8')
# 读取yaml格式的数据内容并保存原有的格式
data = yaml.load(stream=file, Loader=yaml.FullLoader)
print(type(data))
print(data)
print(type(data['b']))
