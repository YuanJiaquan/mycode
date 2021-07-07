
data={'name':'xiao','value':'lixiang'}
def test(**data):
    print(data['name'],data['value'])
test(**data)