import yaml

file=open('H:/python/yaml1/Pytest/class46/data/user.yaml', mode='r', encoding='utf-8')
f=yaml.load(file,Loader = yaml.FullLoader)
print(f)