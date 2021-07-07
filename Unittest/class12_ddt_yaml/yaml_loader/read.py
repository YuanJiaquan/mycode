'''
    读取yaml中的文件内容
'''

import yaml

# 获取文件
file = open('../data/data4.yaml', 'r', encoding='utf-8')
# 读取yaml文件中的内容
data = yaml.load(stream=file, Loader=yaml.FullLoader)
print(data)
