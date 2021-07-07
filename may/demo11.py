# 面向对象：私有的属性，私有的方法  封装，继承，多态，类方法，静态方法

# 私有属性，方法
# 场景：不愿意把对象的方法和属性公开的时候
# 私有属性：不愿意公开属性
# 私有方法：不愿意公开方法

# 定义：属性或者方法的前面 加个__  age=18  __age=18  def open()  def __open()

# class Girl:
#     def __init__(self,name):
#         self.name=name
#         # 不要轻易问女孩子的年龄
#         self.__age=18
#
#     def __desc(self):
#         print('我的年龄是：%d'%self.__age)


# qiushui=Girl('秋水')
# 私有属性，不能在外部调用
# print(qiushui.__age)
# 私有方法，不能在外部调用
# qiushui.__desc()

# 伪私有 并没有真正意义上的私有，还是可以访问到的
# 解决：_类名__名称
# qiushui=Girl('秋水')
# print(qiushui._Girl__age)
# qiushui._Girl__desc()


# 面向对象的特征：封装，继承，多态
# 封装：把对象的细节封装起来  属性和方法封装到抽象类种，创建对象，调用对象种的属性和方法
# 减肥成长记  类和对象
# 小明 体重 80公斤
# 1.小明每次跑步 会减肥0.5公斤
# 2.每次吃东西 体重会增加1公斤

# class Person:
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight
#     def __str__(self):
#         return '我的名字叫%s 体重%f'%(self.name,self.weight)
#
#     def run(self):
#      print('%s跑步'%self.name)
#      self.weight=self.weight-0.5
#
#     def eat(self):
#      print('%s吃东西' % self.name)
#      self.weight = self.weight +1
#
# qiushui=Person('秋水',80)
# qiushui.eat()
# qiushui.run()
# print(qiushui)

# 继承：单继承 多继承
# 继承概念：子类拥有父类的方法和属性
# 作用：实现代码的重用，相同的代码不需要重复编写  两个类
# 动物类：吃  睡  跑
# 狗类：吃  睡  跑  叫
# # 继承：语法 class 类名(父类名):
# class Animal:
#     def eat(self):
#         print('吃')
#     def sleep(self):
#         print('睡')
#     def run(self):
#         print('跑')
# class Dog(Animal):
#     def bark(self):
#         print('叫')
# # 创建一个具体的狗对象
# lucy=Dog()
# lucy.eat()
# lucy.sleep()
# lucy.run()
# lucy.bark()
# 继承可以直接享用父类的方法，不需要再次开发
# 子类在按照自己的需求，封装自己的方法
# 扩展专业的术语：
# Dog类 是Animal类的 子类  Animal类是Dog类的  父类   Dog类从Animal类进行  继承
# Dog类 是Animal类的 派生类  Animal类是Dog类的 基类   Dog类从Animal类进行  派生

# 继承可以一直继承下去  单继承
# A--B--C类  C类会具有A和B所有的属性
# class Animal:
#     def eat(self):
#         print('吃')
#     def sleep(self):
#         print('睡')
#     def run(self):
#         print('跑')
# class Dog(Animal):
#     def bark(self):
#         print('叫')
# class GodDog(Dog):
#     def fly(self):
#         print('我会飞')
# gg=GodDog()
# gg.eat()
# xiaotq=GodDog()
# xiaotq.fly()
# xiaotq.bark()
# xiaotq.run()
# xiaotq.sleep()
# xiaotq.eat()

# class Animal:
#     def eat(self):
#         print('吃')
#     def sleep(self):
#         print('睡')
#     def run(self):
#         print('跑')
# class Dog(Animal):
#     def bark(self):
#         print('叫')
# class GodDog(Dog):
#     def fly(self):
#         print('我会飞')
# class CommonDog(Dog):
#     def catch(self):
#         print('会抓毛球')
#
# xiaotq=GodDog()
# xiaotq.fly()
# xiaotq.bark()
# xiaotq.run()
# xiaotq.sleep()
# xiaotq.eat()


# 问题：哮天犬有抓的功能吗  没有抓的功能  父亲有两个儿子  哮天犬  小七   单继承

# 多继承是什么意思呢
# 子类可以拥有多个父类，并且具有父类所有的属性和方法  一个孩子 有爸爸也有妈妈
# 多继承的语法：class 类名(父类,父类,。。。。)
# class A:
#     def demoA(self):
#         print('demoA 方法')
# class B:
#     def demoB(self):
#         print('demoB方法')
#
# class C(A,B):
#     def demoC(self):
#         print('demoC方法')
# # 创建出一个儿子
# c=C()
# c.demoC()
# c.demoB()
# c.demoA()
# # 不建议用多继承

# 继承 的重写
# 什么时候会用到重写呢？父类的方法不能满足子类的需求的时候，就会用到重写
# 重写，直接覆盖父类的方法，在子类中重新编写
# 扩展，在父类的基础上在扩展自己想要的内容
# class Animal:
#     def eat(self):
#         print('吃')
#     def sleep(self):
#         print('睡')
#     def run(self):
#         print('跑')
# class Dog(Animal):
#     def bark(self):
#         print('叫')
# class GodDog(Dog):
#     def fly(self):
#         print('我会飞')
#     def bark(self):
#         print('叫的你听不懂，跟神一样的叫')
# xtq=GodDog()
# xtq.bark()

# 对父类的方法扩展：子类的方法包含父类的实现方法，又有子类的实现
# super()父类的方法
# class Animal:
#     def eat(self):
#         print('吃')
#     def sleep(self):
#         print('睡')
#     def run(self):
#         print('跑')
# class Dog(Animal):
#     def bark(self):
#         print('叫')
# class GodDog(Dog):
#     def fly(self):
#         print('我会飞')
#     def bark(self):
#         print('叫的你听不懂，跟神一样的叫')
#         # 调用父类的方法
#         # super().bark()
#         # 写法 父类名.方法
#         Dog.bark(self)
#         print('是这么叫的giehgiehigowhghew')
#
# xtq=GodDog()
# xtq.bark()

# 问题：基础后，父类有私有属性，子类能访问吗
# class A:
#     def __init__(self):
#         self.num1=100
#         self.__num2=200
#     def __test(self):
#         print('私有方法%d %d'%(self.num1,self.__num2))
#     def open(self):
#         print('公开方法%d %d' % (self.num1, self.__num2))
# class B(A):
#     def demo(self):
#         # 能访问私有属性和方法吗？
#         # 不能访问私有属性
#         # print('私有属性%d'%self.__num2)
#         # # 不能访问私有方法
#         # self.__test()
#         pass
# b=B()
# b.open()

# 多态：指的同一类型的对象调用同一个方法，表现不同的行为，就是多态

# class Dog:
#     def __init__(self,name):
#         self.name=name
#     def game(self):
#         print('%s蹦蹦跳跳的玩耍..'%self.name)
#
# class GodDog(Dog):
#     def game(self):
#         print('%s飞到天上去玩耍..' % self.name)
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def with_dog(self,dog1):
#         print('%s和%s玩耍'%(self.name,dog1.name))
#
# # 创建一个狗对象
# # erdog=Dog('二狗')
# xtq=GodDog('哮天犬')
# print(xtq.name)
# xtq.game()
# # 创建一个人对象
# zhongling=Person('钟灵')
# print(zhongling.name)
# zhongling.with_dog(xtq)

# 类方法：想访问类属性 调用类方法  要求是 类到底创建了多少个对象

# @classmethod  cls

class Tool:
    # 对象记录器
    count=0
    def __init__(self,name):
        self.name=name
        # 针对类属性做一个计数器
        Tool.count+=1
    @classmethod
    def show_count(cls):
        print('工具对象的数量%d'%cls.count)

# self.count  自己的  1

tools1=Tool('锄头')

tools2=Tool('斧头')
Tool.show_count()


# tools1.show_count()
#
#
# print(tools2.show_count())




# 静态方法  staicMethod   run()没有self
class Dog:
    @staticmethod
    def run():
        print('小狗要乱跑')
Dog.run()

# 类方法：@classmethod  方法中自带cls，然后什么情况用，内部只需要访问类属性的时候就可以用类方法，不用实例化
# 静态方法：@staticmethod 方法中什么都没有，然后什么情况用，不需要访问 实例的属性和类属性的时候，不用实例化

# 提问：  方法内部又要访问实例属性又要访问类属性，应该定义成什么方法
# 实例对象



