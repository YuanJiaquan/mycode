import yaml


file=open('data.yaml', 'r', encoding='utf-8')
data=yaml.load(stream=file)
print(type(data))
print(data)