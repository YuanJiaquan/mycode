# 文件处理和os模块

# 为什么要学文件处理:操作:打开,关闭,读取文件,写入数据
# 文件的作用：就是存储数据，方便下一次从文件中直接读取

# 体验一下文件的基本操作：
# 1.打开文件   open(文件路径,访问模式)
# 主模式：r 只读，w 只写，a,只写
# r+:在r的基础上新增了可写的功能,w+在w的基础上增加了可读的功能,a+:在写的功能上增加了可读的功能
# rb,wb用于二进制文件
# 2.写入文件，读取文件
# 3.关闭文件 文件对象.close() 占用服务器资源

# f=open('test.txt','w')
# f.write("""aaaa
# bbbbb
# cccc
# """)
# f.close()

# r，如果文件不存在，会报错,只读
# # f=open('test1.txt','r')
# f=open('test.txt','r')
# # print(f.read())
# f.write('wwwww')
# f.close()

# w表示只写，如果文件不存在，新建文件,会覆盖与哪有的内容
# f=open('test1.txt','w')
# f.write('aaa')
# f.close()

# a表示只写，如果文件不存在，新建文件,不会覆盖，会在后面追加新的内容
# f=open('test2.txt','a')
# f.write('bbbbb')
# f.close()

# r+:没有提前文件一样会报错，写入内容，会覆盖之前的内容，r+的文件指针在开头,可读可写
# f=open('test2.txt','r+')
# # 文件指针在哪  tell
# print(f.tell())
# # print(f.read())
# f.write('aa')
# f.close()

# w+:没有创建文件会新建，可读又可写,每次把之前的内容覆盖掉，文件指针,写完之后指针在尾部
# 现在读取能读到数据吗？非要读取 seek偏移 seek(偏移量,指针位置)0从头开始读，1：当前位置，2结尾
# f=open('test3.txt','w+')
# f.write('qiushui')
# # print(f.tell())
# # f.seek(2,0)
# print(f.read())
# f.close()

# a+:新建文件,指针位置,a+在最后加内容，可读和可写
# f=open('test4.txt','a+')
# f.write('sandishui')
# print(f.tell())
# print(f.read())
# f.close()

# 路径：扩展一下
# 1.目录下的同文件  ./当前目录
# f=open('./test4.txt','r')
# print(f.read())
# f.close()

# 2.文件目录下的文件，访问外层文件目录下的文件,跨目录访问  ../
# 相对路径，   绝对路径：详细地址D:\vip\vvipclass01
# f=open('../class06/test1.txt','r')
# print(f.read())
# f.close()

# 3.同级目录 ./  目录名/文件名


# 读取文件  read(字符数)  readline()  readlines()
# f=open('test1.txt','r')
# # print(f.read())
# print(f.read(5))
# f.close()

# 只读取一行数据
# f=open('test1.txt','r')
# print(f.readline())

# 读取到所有的数据
# f=open('test1.txt','r')
# print(f.readlines())

# 指定读取
# print(f.readlines()[1])

# print(f.readlines())配套for循环
# f=open('test1.txt','r')
# for i in f.readlines():
#     print(i)
# f.close()

# with..open()as 可以不用关闭文件  as别名
'''
with open(路径，模式)as 变量:
    文件操作
'''
# with open('test1.txt','r')as f:
#     print(f.read())

# f=open('test1.txt','w')
# f.write('qiushui')
# f.close()

# os模块：处理文件或文件目录的
# 1.直接导入
import os
# 路径转义：用r或者\\
import shutil

file1='D:\\vip\\vvipclass01\\class07_Key\\aa'
# 创建一个文件目录
# os.mkdir(file1)

# 删除文件
# os.rmdir(file1)

# 删除非空文件
# shutil.rmtree(file1)

# 重命名
# os.rename(r'D:\vip\vvipclass01\class07_Key\aa',r'D:\vip\vvipclass01\class07_Key\bbb')

# 获得当前文件夹路径 os.getcwd
# print(os.getcwd())
# 当前文件的路径 os.path.join()
# path1=os.getcwd()
# print(path1)
# demo7='demo7.py'
# print(os.path.join(path1,demo7))

# 获取文件权限 os.access(path,mode)
# F_OK(是否存在)，R_OK(可读) w_ok(可写) X_OK(可执行)

# file2=r'D:\vip\vvipclass01\class07_Key\test.txt'
# # print(os.access(file2,os.F_OK))
# print(os.access(file2,os.R_OK))
# print(os.access(file2,os.W_OK))
# print(os.access(file2,os.X_OK))

# os.chmod