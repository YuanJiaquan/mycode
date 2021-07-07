# 1.写函数，接收两个数字参数，返回最大值
# 例如：
# 传入：10,20
# 返回：20
def max1(a,b):
    if a>=b:
        return a
    else:
        return b
print(max1(10,20))
#
# 2.写函数，获取传入列表的所有奇数位索引对应的元素，并将其作为新列表返回。
# 例如：
# 传入：[34,23,52,352,352,3523,5]
# 返回：[23,352,3523]
def a2(l):
    li=[]
    for i in range(len(l)):
        if i%2==1:
            li.append(l[i])
    return li
l2=[34,23,52,352,352,3523,5]
print(a2(l2))
#
# 3.写函数，判断用户传入的对象（列表）长度是否大于5，如果大于5，那么仅保留前五个长度的内容并返回。不大于5返回本身。
# 例如：
# 传入1：[34,23,52,352,666,3523,5]   	返回1：[34,23,52,352,666]
# 传入2：[34,23,52]     				返回2：[34,23,52]
def a3(l):
    li=[]
    if len(l)>5:
        for i in range(5):
                li.append(l[i])
    else:
        li=l
    return li
l31=[34,23,52,352,666,3523,5]
l32=[34,23,52]
print(a3(l31))
print(a3(l32))
#
# 4.写函数，检查传入的字符串是否含有空字符串，返回结果，包含空字符串返回True，不包含返回False
# 例如：
# 传入："hello world"
# 返回：True
def a4(s):
    ret=False
    for i in s:
        if i==' ':
            ret=True
            break
    return ret
print(a4("hello world"))
#
# 5.写函数，接收n个数字，求这些数字的和
def a5(*args):
    return sum(args)
print(a5(5,6,8,6))
#
# 6.定义一个函数,实现两个数四则运算,要注意有3个参数,分别是运算符和两个运算的数字.
# 例如：
# 传入：10,*,20
# 返回：200
def a(a,b,fh):
    return eval(str(a)+str(fh)+str(b))
print(a(10,20,'*'))
#
# 7.实现学生管理系统,完成对学员的增,删,改,查和退出学生管理系统。
# 要求1：使用一个list用于保存学生的姓名。
# 要求2：输入0显示所有学员信息,1代表增加，2代表删除，3代表修改，4代表查询，exit代表退出学生管理系统。每一个功能定义一个自定义函数。界面如下：
# 系统界面如下：
# -----------------------欢迎进入T666班学生管理系统-----------------------------
# 请选择系统功能：
# 0:显示所有学员信息
# 1:添加一个学员信息
# 2:删除一个学员信息
# 3:修改一个学员信息
# 4:查询一个学员信息
# exit:退出学生管理系统

#
# (0)输入0后效果如下：
# 	0
# 	["郭易","汤碗珍"..]
#
# (1)输入1后效果如下：
# 	1
# 	请输入增加人的姓名：张三
# 	["郭易","汤碗珍",'张三'..]
#
# (2)输入2后效果如下：
# 	2
# 	请输入删除人的姓名：张三
# 	["郭易","汤碗珍"..]
#
# (3)输入3后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
# 	3
# 	请输入需要修改人的姓名：张三
# 	请输入需要修改后的姓名：李四
# 	["郭易","汤碗珍",'李四'..]
#
# (4)输入4后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
# 	请输入查询人的姓名：张三
# 	郭易在座位号(3<下标>)的位置。
#
# (5)输入exit后效果如下：
# 	exit
# 	欢迎使用T666的学生管理系统，下次再见。
#

# l=['张三','李四','王麻子','张大妈','王大妈']
# d={0:'显示所有学员信息',1:'添加一个学员信息',2:'删除一个学员信息',3:'修改一个学员信息',
#    4:'查询一个学员信息','exit':'退出学生管理系统'}
# for i,j in d.items():
#     print(i,j)
# def show_all():
#         print(l)
# def add_xueyuan():
#         l.append(input('添加学员姓名：'))
#         print(l)
# def de_xueyuan():
#         l.remove(input('删除学员姓名'))
#         print(l)
# def update_xueyuan():
#         oldname = input('请输入需要修改人的姓名: ')
#         newname = input('请输入需要修改后的姓名: ')
#         if l.count(oldname) > 0:
#             l[l.index(oldname)] = newname
#             print(l)
#         else:
#             print('T666班没有这个学员!!!')
# def search_xueyuan():
#         sea=input('请输入查询学员姓名：')
#         print(l[l.index(sea)])
# def exi():
#         print('欢迎使用T666的学生管理系统，下次再见。')
#         quit()
# def a2(a):
#     if a=='0':
#         show_all()
#     elif a=='1':
#        add_xueyuan()
#     elif a=='2':
#         de_xueyuan()
#     elif a=='3':
#         update_xueyuan()
#     elif a=='4':
#         search_xueyuan()
#     elif a=='exit':
#         print('欢迎使用T666的学生管理系统，下次再见。')
#         quit()
#     else:
#         print('输入有误!!!')
#
# a2(input('请选择系统功能：'))

def getallinfo():
    print(mylist)
    #a2(input(str1),mylist)

def addinfo():
    mylist.append(input('请输入增加人的姓名：'))
    print(mylist)
    #a2(input(str1),mylist)

def delinfo():
    delname = input('请输入删除人的姓名：')
    if mylist.count(delname) > 0:
        mylist.remove(delname)
        print(mylist)
    else:
        print('T666班没有这个学员!!!')
    #a2(input(str1),mylist)

def updateinfo():
    oldname = input('请输入需要修改人的姓名: ')
    newname = input('请输入需要修改后的姓名: ')
    if mylist.count(oldname) > 0:
        mylist[mylist.index(oldname)] = newname
        print(mylist)
    else:
        print('T666班没有这个学员!!!')
    #a2(input(str1), mylist)

def selectinfo():
    selectname = input('请输入查询人的姓名:')
    if mylist.count(selectname) > 0:
        print(selectname, '在座位号' + str(mylist.index(selectname)) + '的位置')
    else:
        print('T666班没有这个学员!!!')
    #a2(input(str1),mylist)

def a2(num,mylist):
    if num=='0':
        getallinfo()
    elif num=='1':
       addinfo()
    elif num=='2':
        delinfo()
    elif num=='3':
        updateinfo()
    elif num=='4':
        selectinfo()
    elif num=='exit':
        print('欢迎使用T666的学生管理系统，下次再见。')
    else:
        print('输入有误!!!')
        a2(input(str1),mylist)
mylist=["郭易","汤碗珍"]
str1=input()
#str1=a2(input(),mylist=[])
a2(str1,mylist)
#print(str1)
