# 1、任意的输入10个数字，按从大到小排序
l1=list(map(int,input().split(' ')))
l1.sort()
print(l1)
# 2、"在一个月黑风高的夜晚，一个小男生用自己的零花钱给小女生买了一束鲜花，小女生问小男生鲜花的数量:“这花多少束?”，通过键盘输入小男
# 孩回答的鲜花的束数，数量不一样小女生的反应也不一样。如果鲜花数大于等于9999，打印："小女生直接晕了过去",如果在1000(包含)-9999
# (不包含)，打印："明天就结婚",如果在100(包含)-1000(不包含)，打印："拉拉手意思意思，有空再约！",否则：打印："你是个好人"
print('在一个月黑风高的夜晚，一个小男生用自己的零花钱给小女生买了一束鲜花，小女生问小男生鲜花的数量:“这花多少束?')
s=int(input('男孩回答：'))
if s>=9999:
    print('小女生直接晕了过去')
elif s in range(999,9999):
    print('明天就结婚')
elif s>=100 and s<1000:
    print('拉拉手意思意思，有空再约！')
else:
    print('你是个好人')

# 3、输入三角形的三条边长，判断三角形的类型。根据实际情况分别打印：
# 不能构成三角形，一般三角形，等腰三角形，等边三角形，只要能构成三角形，则还需要计算出：周长。

l3=list(map(int,input('输入三角形三边长度以空格分隔:').split(' ')))
l3.sort()
c=0
if l3[2]<l3[0]+l3[1] :
    c = l3[0] + l3[1] + l3[2]
    if l3[2]==l3[0] and l3[0]==l3[1]:
        print('等边三角形,周长为：%d'%c)
    elif l3[0]==l3[1]:
        print('等腰三角形，周长为：%d'%c)
    else:
        print('一般三角形，周长为：%d'%c)
else:
    print('不能构成三角形')

# 4、如果输入三个不同的数，要求比较大小并按从小到大排序输出呢？如输出：a<b<c）
l4=list(map(int,input('输入三个数字以空格分隔:').split(' ')))
l4.sort()
print(l4)

# 5、判断输入的用户名为admin及密码为admin则打印登录成功，否则打印用户名或密码错误，登录失败
s51=input('请输入用户名：')
s52=input('请输入用户密码：')
if s51=='admin' and s52=='admin':
    print('登录成功')
else:
    print('用户名或密码错误，登录失败')

# 6、判断输入的数是奇数还是偶数
a6=int(input('输入一个数字：'))
if a6%2==0:
    print('输入的数字为偶数')
else:
    print('输入的数字为奇数')


# 7、用户输入的年份是否为闰年
from operator import __abs__
a7=int(input('输入年份：'))
a71=__abs__(a7-2000)
if a71%4==0:
    print('%d为闰年'%a7)
else:
    print('%d不为闰年'%a7)
# 8、python实现石头剪刀布的游戏。
# 1.从控制台输入要输出的拳--石头（1）剪刀2、布3
# 2.电脑随机出拳--假定电脑只会出石头
# 3.比较胜负
import random
d81=['剪刀','石头','布']
print(d81)
s8=input('请选择：')
d8={1:'剪刀',2:'石头',3:'布'}
x=list(d8.keys())[list(d8.values()).index(s8)]
y=random.randrange(1,4,1)
print(x,y)
if x==y:
    print('重出')
elif x+1==y or x==y+2:
    print('电脑获得胜利')
else:
    print('您获得胜利')

# 9.判断某一个字典中是否存在指定的值，如果存在，提示并且退出循环
# 如果不存在，在循环整体结束后，得到一个统一的提示
# students=[{'name':'二狗','age':20,'height':1.7,'weight':75},{'name':'狗蛋','age':20,'height':1.7,'weight':75}]
students=[{'name':'二狗','age':20,'height':1.7,'weight':75},{'name':'狗蛋','age':20,'height':1.7,'weight':75}]

# 判断二狗在不在
for x in range(len(students)):
    for i,j  in students[x].items():
        if j=='二狗':
            print('存在')
        else:
            pass
#
# 10.打印99乘法表
for i in range(1,10):
    l = []
    for j in range(1,i+1):
        l.append(i*j)
    print(l)

# 11、打印如下图案：
# *
# **
# ***
# ****
# *****
for  i in range(1,6):
    print(i*('*'))

# 12、打印如下图案：
# *
# ***
# *****
# *******
# *********
for  i in range(1,10,2):
    print(i*('*'))

# 13、打印如下图案：
# #####*
# ####***
# ###*****
# ##*******
# #*********

for  i in range(1,10,2):
    x=11-i
    y=x//2
    print(y*('#')+i*('*'))

# 14、打印如下图案：
#      *
#     ***
#    *****
#   *******
#  *********
#   *******
#    *****
#     ***
#      *

s = '*'
for  i in range(1,10,2):
    print((i*s).center(9))
for  i in reversed(range(1,8,2)):
    print((i*s).center(9))
#
# 15、定义一个List，任意输入10个数字保存到List，然后按从小到大排序。（冒泡排序）
#
l=[11,2,8,6,5,4,1,20,9,3]
for j in range(1,11):
    for i in range(len(l)-j):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
        else:
            pass
print(l)