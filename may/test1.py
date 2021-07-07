# import os
# import csv
#
# f=open('test.csv','a')
# stu1=[4,'djy',18,'
# class04_等待']
# stu2=[5,'djy2',18,'class05']
#
# # f=open('456.csv','a',newline='')
# # # 写数据
# w=csv.writer(f,dialect='excel')
# # # 具体写入csv的数据
# w.writerow(stu1)
# w.writerow(stu2)
#
# print(os.getcwd())
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print("%s: %s" % (self.name, self.score))
# stu=Student('xiaoming',99)
# stu.print_score()
# stu1=Student('xiaohong',98)
# stu1.print_score()