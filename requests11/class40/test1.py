import yaml

file=open('./dd1.yaml', mode='r', encoding='utf-8')
data=yaml.load(stream=file, Loader=yaml.FullLoader)

print(data['xiaoming']['have']['other']['color'])