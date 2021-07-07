# 作业

# 上节课：*和**

# 普通参数，占1个坑，传1个参数
# *是可以传多个参数，传过来的参数保存在元组中

# **是可以传个参数，参数，关键字传参  name='xxx'  age='xx',保存在字典中
# def demo1(*args):
#     print(args)
# demo1(1,2,3,4)
# demo1((1,2,3,4),{'name':'qiushui','age':18,'sex':'女'})

# def demo2(**kwargs):
#     print(kwargs)
# demo2(name='qiushui',age='18',sex='女')
# 加了*会变成把数据转成{'name':'qiushui','age':18,'sex':'女'}

# 1，2，3  ，kwargs:name='qiushui',age='18',sex='女'
def demo3(*args,**kwargs):
    # prints是个函数  *args保存成元组（1，2，3）
    print(*args)
    print(**kwargs)
a1=(1,2,3)
a2={'name':'qiushui','age':18,'sex':'女'}
# demo3(a1,a2)
# 这里是个普通参数，args可以接受多个参数
# demo3((1,2,3),{'name':'qiushui','age':18,'sex':'女'})

# 想要把(1,2,3)传给*args，{'name':'qiushui','age':18,'sex':'女'}传给**kwargs
# demo3(1,2,3,name='qiushui',age='18',sex='女')
# 一个字典一个元组
# *和**就是解包  （1，2，3）*a1：1，2，3   {'name':'qiushui','age':18,'sex':'女'}**karges解包:name='qiushui',age='18',sex='女'
demo3(*a1,**a2)


# 一个元组
# 一个元组，一个字典
# 就是一个元组：元组里面有元组和字典，字典为空
# 普通的传参，传过去


