from may2.mysql.mysql import my_db

a=my_db('./db.ini','Test_DB')
s='insert into S(SNO,SNAME,SDD,SA) values(%s,%s,%s,%s)'
# 执行sql
v=([(2019001,'托马斯李','运营',26),(2019002,'米高扬','管理',30),(2019003,'蝙蝠侠','安防',22),(2019004,'李嘉诚','投资',45),
        (2019005,'雷军','开发',34),(2019006,'周小川','管理',56),(2019007,'陆奇','运营',36),(2019008,'普京','安防',67)])
print(a.idumany_db(s,v))
# s='delete from s'
# print(a.idu_db(s))