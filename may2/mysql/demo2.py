# # 查询
# # 连接数据库
import pymysql


# 在别的
def insert_query(query):
    con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='test01')
    # # 创建游标
    cur=con.cursor()
    # sql='select * from emp'
    # 执行sql
    cur.execute(query)
    # 结果需要显示出来  fetchone只会拿出一条数据  fetchmany(条数) 指点拿出的是几条数据
    # fetchall 把所有的数据全部拿出来
    # result=cur.fetchone()
    # result=cur.fetchmany(2)
    result=cur.fetchall()
    # print(result)
    return result

def idu_query(query):
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test01')
    # 创建游标
    cur = con.cursor()
    cur.execute(query)
    # 增删改执行sql要commit
    cur.execute('commit')
    return True

