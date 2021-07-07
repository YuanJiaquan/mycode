import pymysql
try:
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Aa123456',database='db1')
    cur=conn.cursor()
    for i in range(10000):
        sql='insert into s11 (id,name,score) values (%s,%s,%s)'
        value=[(i,"xiaowang",50+i)]
        cur.executemany(sql,value)
        cur.execute('commit')
except Exception as e:
    print(e)

conn.close()
