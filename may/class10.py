# 1.将身边的一个事物抽象出一个类。比如老师、学生、桌子、椅子、苹果、香蕉、枕头、被子或任意物品。
# 1.提供基本属性、基本的方法。
# 2.通过类创建出几个不同的对象。
# 3.打印它们的属性、调用它们的方法。
#
# 2.# 减肥成长记  类和对象
# 小明 体重 80公斤
# 1.小明每次跑步 会减肥0.5公斤
# 2.每次吃东西 体重会增加1公斤

# 邮箱：2804555260@qq.com

class jianfei(object):

    name='xiaoming'
    def __init__(self,weight):
        self.weight=weight

    def run(self):
        self.weight=self.weight-1
    def eat(self):
        self.weight=self.weight+2
Duo=jianfei(180)
"""
三天吃了五次东西，跑了两次步，问现在体重
"""
for i in range(5):
    Duo.eat()
for i in range(2):
    Duo.run()
print(Duo.weight)
