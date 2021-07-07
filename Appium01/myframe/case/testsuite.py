import os
import unittest
from HTMLTestRunner import HTMLTestRunner



discover=unittest.defaultTestLoader.discover(start_dir='../case/', pattern='case1.py')

report_dir='../report'
title = 'DEMO系统的测试报告'
description = '本次是属于0.1版本的首轮冒烟测试执行结果'


if not os.path.exists(report_dir):
    os.mkdir(report_dir)
with open('../report/report.html','wb')as f:
    HTMLTestRunner(stream=f,title=title,description=description,verbosity=2).run(discover)



