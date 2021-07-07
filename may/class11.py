# 一、定义名为MyTime的类，其中应有三个实例变量
# 时hour
# 分minute
# 秒second
# 1）为了给对象初始化赋值，编写构造方法，对时分秒附初始值
# 2）为了保证数据的安全性，这三个成员变量应声明为私有、
# 3）对三个属性分别定义封装get和set方法，定义一个main方法，创建一个MyTime类的对象并调用这六个方法。
class MyTime():
    # def __init__(self,H,M,S):
    #     self.__hour=H
    #     self.__minute=M
    #     self.__second=S
    __hour = 0
    M=0
    S=0
    def set_hour(self,__hour):
        self.__hour=__hour

    def get_hour(self):
        return self.__hour

    def set_minute(self, M):
        self.M = M

    def get_minute(self):
        return self.M

    def set_second(self, S):
        self.S = S

    def get_second(self):
        return self.S
    def main_1(self,a,b,c):
        self.set_hour(a)
        self.set_minute(b)
        self.set_second(c)
        H1=self.get_hour()
        M1=self.get_minute()
        S1=self.get_second()
        print('设置的时间为：%s:%s:%s'%(H1,M1,S1))
if __name__ == '__main__':
    mm = MyTime()
    mm.main_1(10,23,35)
    # mm.set_hour(5)
    # mm.set_second(7)
    # # mm.set_minute(6)
    # # mm.get_hour()
    # mm.get_second()
    # mm.get_minute()
    # mm.get_hour()
#
#
#
# 二、为
# "无名的粉"
# 写一个类WuMingFen，有三个属性
# 面码: String
# theMa
# 粉的分量(两)
# int
# quantity
# 是否带汤
# boolean
# likeSoup
# 要求：
# 1）写一个构造方法
# 分别给三个属性赋值。构造出一个WuMingFen类的对象(酸辣面码、2
# 两、带汤)，
# 2）写一个普通方法check()
# 打印对象的三个属性。通过对象调用此方法。
class WuMingFen:
    theMa=''
    quantity=0
    likeSoup=True
    def set_mianma(self,a,b,c):
        self.theMa=a
        self.quantity=b
        self.likeSoup=c

    def check(self):
        print(self.theMa,self.quantity,self.likeSoup)

w1=WuMingFen()
w1.set_mianma('asd',12,False)
w1.check()
#
#
# 三、摆放家具
# 需求：
# 1）房子有户型，总面积和家具名称列表
# 新房子没有任何的家具
# 2）家具有名字和占地面积，其中
# 床：占4平米
# 衣柜：占2平面
# 餐桌：占1
# .5
# 平米
# 3）将以上三件家具添加到房子中
# 4）打印房子时，要求输出: 户型，总面积，剩余面积，家具名称列表
class put_jiaju:
    x=0
    y=0
    def __init__(self,h,z,j):
        self.h=h
        self.z=z
        self.j=j

    def set_jiaju(self):
        # self.bed=bed
        # self.gui=gui
        # self.can=can
        for i in self.j:
            self.y=self.y+self.j[i]
        return self.y

    def dayin(self):
        self.x=self.z-self.y
        print('户型:%s，总面积:%s，剩余面积:%s，家具名称列表:'%(self.h,self.z,self.x))
        for i in self.j:
            print(i)

jiaju={'床':4,'衣柜':2,'餐桌':1.5}
a=put_jiaju('三室',85,jiaju)
a.set_jiaju()
a.dayin()



# 四、需求：
# 1）士兵瑞恩有一把AK47
# 2）士兵可以开火(士兵开火扣动的是扳机)
# 3）枪能够发射子弹(把子弹发射出去)
# 4）枪能够装填子弹 - -增加子弹的数量

class gun():
    modle='AK47'
    zidan=0
    max_zidan=30
    def set_gun(self,modle,zidan):
        self.modle=modle
        self.zidan=zidan
        print('获得一把%s和%s发子弹'%(modle,zidan))
    def add_zidan(self):
            if self.zidan < self.max_zidan:
                self.zidan+=10
            else:
                print("子弹已装满")
            return self.zidan
    def fire(self):
        if self.zidan==0:
            print('没有子弹，请先装填子弹')
        else:
            print('%s子弹可以发射'%self.zidan)
            self.zidan-=1
        return self.zidan

class Person(gun):
    def __init__(self):
        self.name='Ruien'

    def option(self):
        if self.zidan>0:
            print('士兵可以开火')
        else:
            print('请先装填子弹')
p1=Person()
p1.set_gun('AK47',0)
p1.option()
p1.add_zidan()
p1.add_zidan()
p1.add_zidan()
p1.option()
p1.fire()

#
# 五、编写程序实现乐手弹奏乐器。乐手可以弹奏不同的乐器从而发出不同的声音。可以弹奏的乐器包括二胡、钢琴和琵琶。
# 实现思路及关键代码：
# 1)定义乐器类Instrument，包括makeSound()
# 方法，此方法中乐器声音："乐器发出美妙的声音！"
# 2)定义乐器类的子类：二胡Erhu、钢琴Piano和小提琴Violin
# 二胡Erhu声音："二胡拉响人生"
# 钢琴Piano声音："钢琴美妙无比"
# 小提琴Violin声音："小提琴来啦"
# 3）用main类，多态的方式对不同乐器进行切换

class Instrument():
    def __init__(self,a):
        self.leixing=a
    def shenying(self):
        print('%s发出美妙的声音！'%self.leixing)

class Erhu(Instrument):

    def shenying(self):
        print('%s二胡拉响人生'%self.leixing)
class Piano(Instrument):
    def shenying(self):
        print('钢琴美妙无比')
class Violin(Instrument):
    def shenying(self):
        print('小提琴来啦')
def a(self):
    self.shenying()

if __name__ == '__main__':

    er=Erhu('ERHU')
    # er.shenying()
    # pi=Piano('GANGQING')
    # pi.shenying()
    a(er)

# 六：设计个一个游戏类
# 定义一个 ‘类属性’top_score
# 记录游戏的历史最高记录
# 定义一个‘ 实例属性’player_name
# 记录当前游戏的玩家姓名
# ‘静态方法’show_help显示游戏帮助信息
# ‘类方法’show_top_score显示历史最高分
# ‘实例方法’start_game开始当前玩家的游戏
# 步骤：
# 1.
# 查看帮助信息
# 2.
# 查看历史最高分
# 3.
# 创建游戏对象，开始游戏

class Game:
    top_score = 0
    def __init__(self,name,score):
        self.player_name=name
        Game.top_score = score
    @staticmethod
    def show_help():
        print('游戏帮助信息')
    @classmethod
    def show_top_score(cls):
        print('历史最高分%s'%cls.top_score)
    def start_game(self):

        print('玩家%s本次游戏得分%s'%(self.player_name,self.top_score))

Game.show_help()
Game.show_top_score()
game=Game('钟灵',99)
game.start_game()
Game.show_top_score()