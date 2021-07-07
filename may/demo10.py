# 面向对象
# 万物皆对象
# 面向对象：面向对象编程—— Object Oriented Programming 简写 OOP：是一种封装代码的写法
# 面向对象，面向过程的基础上发展出来的，面向对象比面向过程更加灵活和有扩展性
# 面向过程：
# 面向对象：
# 猜过迷：把大象放进冰箱需要几步：
# 1.打开冰箱
# 2.把大象装进冰箱
# 3.关闭冰箱门
#
# def open():
#     pass
# def into():
#     pass
# def close():
#     pass
# 面向过程：就是有一个需求，按照这个需求，逐步去写。独立功能封装，最后有顺序的调用  1

# 面向对象：冰箱做为一个对象
# 冰箱 打开
# 冰箱  可以装东西 大象
# 冰箱  关闭
# 面向对象：更大的封装，根据你要做的事情，在一个对象中封装多个方法  2  针对于复杂的系统

# 具体的了解面向对象
# 两个核心内容：1.类，2.对象
# 类是具有相同特征的或者说相同行为的事物就叫统称
# 鸟类  水果
# 特征：有翅膀，两只脚，一双眼睛，心脏四室，体温恒定
# 行为：会飞，会吃虫

# 抽象  不能够直接使用。类相当于模板

# 定义类
# class 类名:
#   属性：
#   方法
# 属性就是特征  方法就是他的作用
# 方法：在类中self  def open(self)
# 类名：随意  见名之意  最好是大写  class Test  驼峰命名  TestAbc

# 猫类
# 设计这只猫有什么特点
# 属性：颜色 白色 脚 4只 体重 20kg
# 方法：抓老鼠  爱吃鱼

# class Cat:
#     cat_color='白色'
#     cat_foot=4
#     cat_weight='20kg'
#
#     def eat(self):
#         print('小猫爱吃鱼')
#     def catch(self):
#         print('小猫抓老鼠')
# 具体到猫  变量名=类名()
# tom=Cat()
# tom.eat()
# tom.catch()
# print(tom.cat_color)
# # 用类中的方法 实例类.方法名 .属性名
# jack=Cat()
# jack.eat()
# jack.catch()
# # 有一个问题  两只猫是同一个吗  16进制的地址  id 是十进制的内存地址
# print(tom)
# print(id(tom))
# print(jack)
# print(id(jack))

# self   类中写注释  在类外面也可以定义属性，但是不建议  self代表的是对象本身，谁调用就代表谁
# class Cat:
#     """这是一个猫类"""
#     cat_color='白色'
#     cat_foot=4
#     cat_weight='20kg'
#
#     def eat(self):
#         print('%s小猫爱吃鱼'%self.cat_color)
#     def catch(self):
#         print('%s小猫抓老鼠'%self.name)
# tom=Cat()
# tom.name='tom1'
# tom.eat()
# tom.catch()

# jack=Cat()
# jack.name='jack1'
# jack.eat()
# jack.catch()

# 属性 在方法里面
# init函数函数：init是一个内置方法，专门用来定义一个类具有哪些属性的方法
# 特点：创建对象时会自动调用
# init方法内部使用：self.属性名=属性初始值
# class Cat:
#     def __init__(self):
#         print('这是一个初始化函数')
#         # 定义了cat类创建的所有的猫都会这一个属性name
#         self.name='tom'
#
#     def eat(self):
#         print('%s爱吃鱼'%self.name)
#
# # 具体对象
# jack=Cat()
# jack.eat()
#
# lucy=Cat()
# lucy.eat()

# 不想让所有的猫都叫tom
# 构造参数里面有参数，必须要传参数，实例化时传参
# class Cat:
#     def __init__(self,name):
#         print('这是一个初始化函数')
#         # 定义了cat类创建的所有的猫都会这一个属性name
#         self.name=name
#
#     def eat(self):
#         print('%s爱吃鱼'%self.name)
#
# # 具体对象
# jack=Cat('jack')
# jack.eat()
#
# tom=Cat('tom')
# tom.eat()


# 内置函数  （了解）
# _init_  创建对象时会自动调用这个方法
# _del_ 对象从内存中销毁之前，会被调用方法
# _str_ 返回对象的描述信息  print函数输出

# class Cat:
#     def __init__(self,new_name):
#         self.name=new_name
#         print('%s小猫来了' % self.name)
#     def __del__(self):
#         print('%s小猫走了'%self.name)
#     def __str__(self):
#         return '我是小猫%s'%self.name
#
# tom=Cat('Tom')
# print(tom.name)
# del tom
# print('-'*50)
#
# tom=Cat('Tom')
# print(tom)

# 将身边的一个事物抽象出一个类。比如老师、学生、桌子、椅子、苹果、香蕉、枕头、被子或任意物品。
# 1.提供基本属性、基本的方法。
# 2.通过类创建出几个不同的对象。
# 3.打印它们的属性、调用它们的方法。

# 减肥成长记  类和对象
# 小明 体重 80公斤
# 1.小明每次跑步 会减肥0.5公斤
# 2.每次吃东西 体重会增加1公斤

# 邮箱：2804555260@qq.com