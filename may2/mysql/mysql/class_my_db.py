import configparser

import pymysql

class my_db:
    def __init__(self,configPath,db):

        config = configparser.ConfigParser()
        # 从配置文件里读取数据库服务器IP  账号 密码.....
        config.read(configPath)
        host = config[db]['host']
        port = int(config[db]['port'])
        user = config[db]['user']
        passwd = config[db]['passwd']
        database = config[db]['database']
        charset = config[db]['charset']
        try:
            self.con=pymysql.connect(host=host,port=port,user=user,password=passwd,database=database,charset=charset)
            self.cur=self.con.cursor()
        except Exception as e:
            print(e)

    def query_db(self,sql):
        try:
            self.cur.execute(sql)
            results=self.cur.fetchall()
            return results
        except Exception as e:
            print(e)
    def idu_db(self,sql):
        try:
            self.cur.execute(sql)
            result=self.cur.fetchall()
            self.cur.execute('commit')
            return  True
        except Exception as e:
            print(e)

    def idumany_db(self,sql,value):
        try:
            self.cur.executemany(sql,value)
            result=self.cur.fetchall()
            self.cur.execute('commit')
            return  True
        except Exception as e:
            print(e)
    def __del__(self):
        self.con.close()