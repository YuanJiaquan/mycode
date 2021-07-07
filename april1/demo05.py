# 函数：就是把具有独立功能的代码块，组织成一个小的模块。
# 函数两个步骤：
# 1.定义函数--封装成一个独立的功能
# 2.调用函数--享受  封装 的成功  方法名()
# 函数的作用：可以提高编码的效率--重用
# 函数的格式
'''
def 函数名(参数1,参数2，参数3):
    封装的代码
    :return
# 调用：函数名() 返回给调用者
'''
# 注意：def 关键字必须要填，函数名，随意命名，见名之意,不能以数字开头，不能以关键字冲突

# 第一个函数的演练
# def say_hello():
#     print('hello 1')
#     print('hello 2')
#     print('hello 3')
# say_hello()
# 只有调用函数的时候，函数才会被执行

# 练习题目：实现两个数字求和的功能
# def sum1():
#     num1=10
#     num2=20
#     result=num1+num2
#     print('%d+%d=%d'%(num1,num2,result))
# sum1()
# 思考：只能处理固定数值。可不可以用的时候在传过来，函数传参  %d整数
# def sum1(num1,num2):
#     result=num1+num2
#     print('%d+%f=%f'%(num1,num2,result))
# sum1(30,40.2)
# 参数的作用：针对不同的数据进行相同的逻辑处理
# 扩充：术语：函数里面的参数叫形参，在方法调用里面就叫实参

# 完整的函数，实际上会有返回值关键字 return
# 在开发的过程中，有时候我们会需要一个函数运行的最终结果，这个结果就可以通过return返回过来
# def sum2(num1,num2):
#     return num1+num2
# # sum2(1,2) 值3  把3赋值给result
# result=sum2(1,2)
# print(result)

# 空函数，是一个完整的函数  没有实际的意义，预留一个位置
# def empty():
#     pass
# 函数的参数：必须参数，关键字参数，默认的参数，不定长参数
# 必须参数：必须以正确的顺序传入参数，调用的时候必须和申明的一致
# 定义一个人的参数
# def person(name,age):
#     return '我是{},今年{}岁'.format(name,age)
# person1=person('小明',18)
# print(person1)

# 关键字参数，可以通过关键字传参，不用按照顺序去写
# def person(name,age):
#     return '我是{},今年{}岁'.format(name, age)
# person2=person(age=19,name='小明')
# print(person2)

# 默认参数：在定义的过程中设置默认值
# def person(name='虚竹',age=108):
#     return '我是{},今年{}岁'.format(name, age)
# 直接调用函数，可以不用参数
# person3=person()
# print(person3)
# 如果说有默认值，会把原来的值覆盖掉
# person4=person(name='剑来')
# print(person4)
# 如果位置参数和关键字参数同在，先写位置参数，在写默认参数  点进方法
# def person(name,age=108):
#     return '我是{},今年{}岁'.format(name, age)
# a=person('小A',age=109)
# print(a)
# 不定长参数
# 在定义的过程中不知道有多少个参数，设置成不定长度的参数,不确定多少个参数
# 不定长度的参数有两种写法，*  另外一个**
# 在参数前面带一个* 把参数放在元组里面
# def person(name,*args):
#     print(name,end='')
#     print(args)
# person('虚竹',90,'妖','漂亮')

# *单独出现，在调用的时候通过关键字调用
# def a(num1,num2,*,num4):
#     return num1+num2+num4
# print(a(6,7,num4=7))

# def peson(*args):
#     print(args)
# peson(9,10,'小明','消费')

#  **不定长度，可以传多个参数，参数是字典形式
# def a3(**kwargs):
#     print(kwargs)
# a3(name='张三',age='李四')

# *和**同时存在  加*会报错  把数据进行解包,会按照一定的格式去解析数据
# 在函数的参数中*args把数据转成元组的形式，**kwargs要传一个字典的格式
# *是解析元组，**是解析字典
# def a4(*args,**kwargs):
#     print(*args)
#
# # a4(1,2,'qiushui',name='sunny0503',age=18)
# a1=(1,2,3)
# a2={'name':'qiushui','age':'18'}
# a4(a1,a2)

# 函数嵌套 函数中在嵌套函数
# 两个函数  test1(),test()
# def test1():
#     print('*'*50)
#     print('test1')
#
# def test2():
#     print('-'*50)
#     print('test2')
#     test1()
#     print('+'*50)
# test2()




# 匿名函数
# lambda 表达式
# 语法：lambda 参数,参数:表达式
# 匿名函数和普通函数
# 求和
# def sum2(num1,num2):
#     return num1+num2
# result=sum2(1,2)
# print(result)
#
# sum=lambda a,b:a+b
# print(sum(1,2))

# 模块  py文件也就是python文件，我想要用另外一个模块中的方法，
# 先拿到模块，在拿里面的方法


# 留个知识点 *和**  2.递归。。正则  3.下节课，讲之前的作业  听重点几个题目
# 群文件