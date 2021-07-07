import pymysql

conn=pymysql.connect(host='192.168.3.45',port=3306,user='root',password='Aa123456',database='db1')
cur=conn.cursor()
sql='show tables'
cur.execute(sql)
cur.execute('commit')
conn.close()
