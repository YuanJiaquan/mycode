
import yaml
f=open('../data/login.yaml', mode='r',  encoding='utf-8')
data=yaml.full_load(f)
print(data[0]['uname'])
try:
    assert data[0]['uname']=='qwerty26641','失败'
except Exception as e:
    print(e)
print(123)
#
# def test(*data):
#     print(data)
#
# a={'a':1,'b':2}
# b=[1,2,3]
# c=(1,2,3)
#
# test(a)