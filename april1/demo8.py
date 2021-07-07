#_*_ coding:UTF-8_*_
# 文件处理：文件打开，读取写入，关闭  os模块
# 具体应用
# 1.txt
# 2.csv
# 3.xml
# 4.excel，yaml文件学web自动化

# 1.txt
# 文件读取
# 1.打开  open(路径，模式)  with open() as 变量名:
# 2.读取文件/写入文件  read()  readline()  readlines()  write
# 3.关闭

# 读取txt文件  utf-8国际编码
# f=open('123.txt','r',encoding='utf-8')
# # print(f.readlines())
# # f.close()
#
# # 把列表中的数据都读取出来  for循环 ,加个需求：名字读取出来,字符串分割,返回列表  列表怎么取值 qiushui  xuzhu
# for i in f.readlines():
#     # print(i)
#     # print(type(i))
#     # print(i[2])
#     print(i.split(',')[1])
#
# f.close()

# 不用关闭  需求：把名字和年龄输出来  用切片  左闭右开
# with open('123.txt','r',encoding='utf-8')as f:
#     a=f.readlines()
#     print(a)
#
# for i in a:
#     # print(i)
#     print(i.split(',')[1:3])

# 2.csv本质是文本，文本方式，也是,隔开  excel,存储方式表格文件格式  表格:openpyxl,pandas,xlrd
# 读取csv，需要导包  reader()  文件对象 获得数据，for循环  想要获得qiushui，xuzhu
# 列表是怎么取值的
import csv

# f=open('456.csv','r',encoding='utf-8')
# # print(csv.reader(f))
# f2=csv.reader(f)
# for i in f2:
#     # print(i)
#     print(i[1])
#
# with open('456.csv','r',encoding='utf-8') as f:
#     a=f.readlines()
#
# for i in a:
#     print(i)

# csv中写入数据
# stu1=[4,'djy',18,'class04_等待']
# stu2=[5,'djy2',18,'class05']
#
# # a追加文件后面
# # 打开文件  ctrl+鼠标
# f=open('456.csv','a',newline='')
# # 写数据
# writ1=csv.writer(f,dialect='excel')
# # 具体写入csv的数据
# writ1.writerow(stu1)
# writ1.writerow(stu2)

# xml文件的读写，和html比较类似
# html用来显示数据  html就是页面的内容，图片，输入框按钮，css，输入框按钮摆放位置，布局
# js:动态效果

# 读取xml中的数据 导包
from xml.dom import minidom
# 1.加载xml文件
dom=minidom.parse('stu.xml')
# 2.文件数据
root=dom.documentElement
# 获得根节点
# print(root.nodeName)
# # 获得类型  节点的类型是1
# print(root.nodeType)

# 不加s:获得一个和s 获得所有  元素的标签名 getElementsByTagName
# name1=root.getElementsByTagName('name')
# print(name1[0].nodeName)
# age1=root.getElementsByTagName('age')
# print(age1[1].nodeName)

# 想要获得标签的值，节点的值  先拿到标签，在拿到值.firstChild.data
# name1=root.getElementsByTagName('name')
# print(name1[0].nodeName)
# print(name1[0].firstChild.data)

# 前端代码工具 sublime
# 获得属性值：getAttribute
# input所有的标签
# input1=root.getElementsByTagName('input')
# # input第一个标签的属性
# user=input1[0].getAttribute('username')
# print(user)

# 做个题目
# 想要一次性拿到所有学生的信息的值
# student都拿到
# stu=root.getElementsByTagName('student')
# # print(stu)
# # 拿到学生对象里面的name,age,phone
# name1=root.getElementsByTagName('name')
# age1=root.getElementsByTagName('age')
# phone1=root.getElementsByTagName('phone')
# # 所有学生的值，循环
# for i in range(3):
#     print(name1[i].firstChild.data)
#     print(age1[i].firstChild.data)
#     print(phone1[i].firstChild.data)

# 做个题目  只拿ID="S001" 的值
# student都拿到
stu=root.getElementsByTagName('student')
# print('获取所有学生信息%s'%stu)  循环
for i in stu:
    # name 元素
    name1=i.getElementsByTagName('name')[0]
    print(name1.firstChild.data)
    age1 = i.getElementsByTagName('age')[0]
    print(age1.firstChild.data)
    phone1 = i.getElementsByTagName('phone')[0]
    print(phone1.firstChild.data)

# 拿到所有学员的值，这个只拿ID="S001" 的值

# stu=root.getElementsByTagName('student')[0]
# print(stu)
# # print('获取所有学生信息%s'%stu)  循环
# name1=stu.getElementsByTagName('name')[0]
# print(name1.nodeName)
# print(name1.firstChild.data)
#
# age1=stu.getElementsByTagName('age')[0]
# print(age1.nodeName)
# print(age1.firstChild.data)