# python连接数据库
# 需要安装数据库 的模块  pip install pymysql

import pymysql

# 用python代码操作数据库
# 1.连接数据库
# 2.操作数据库 游标 curson 创建
# 3.关闭数据库

# 连接数据库
# con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='test01')
# # 创建游标
# cur=con.cursor()
# # sql='insert into dept(name) values("测试部2")'
# # sql2='update dept set name="测试部3" where id=13'
# sql3='delete from dept where id=13'
# # 执行sql
# cur.execute(sql3)
# # 增删改执行sql要commit
# cur.execute('commit')
# # 关闭数据库
# con.close()

# # 查询
# # 连接数据库
# con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='test01')
# # # 创建游标
# cur=con.cursor()
# sql='select * from dept'
# # 执行sql
# cur.execute(sql)
# # 结果需要显示出来  fetchone只会拿出一条数据  fetchmany(条数) 指点拿出的是几条数据
# # fetchall 把所有的数据全部拿出来
# # result=cur.fetchone()
# # result=cur.fetchmany(2)
# result=cur.fetchall()
# print(result)


# 批量增加数据

# 连接数据库
con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='test01')
# 创建游标
cur=con.cursor()
sql='insert into dept(name) values(%s)'
# 执行sql
value=([('研发部2'),('研发部3')])

cur.executemany(sql,value)
# 增删改执行sql要commit
cur.execute('commit')
# 关闭数据库
con.close()

# 想在别的文件使用  应该怎么办 封装