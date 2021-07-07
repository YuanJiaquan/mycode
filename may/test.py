
# 1.将身边的一个事物抽象出一个类。比如老师、学生、桌子、椅子、苹果、香蕉、枕头、被子或任意物品。
# 1.提供基本属性、基本的方法。
# 2.通过类创建出几个不同的对象。
# 3.打印它们的属性、调用它们的方法。
#
class Any_thing(object):
    # def __init__(self):
    people1='teacher'
    # def __del__(self):
    #     print('nihao')

    def dayin(self):
        print(self.people1)
# a=Any_thing()
# print(a.people1)
# a=Any_thing('xiaohuang','sunmou')
# print(a.people1)
# a.dayin()
a=Any_thing()
a.dayin()
b=Any_thing()
b.dayin()


# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#     def print_score(self):
#         print("%s: %s" %(self.__name,self.__score))
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
# student = Student('Hugh', 99)
# student.get_name()
#
# class Test:
#     def ppr(self):
#         print(self)
#         print(self.__class__)
#
# t = Test()
# t.ppr()


