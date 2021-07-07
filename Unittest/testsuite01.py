import os
import unittest
from HTMLTestRunner import HTMLTestRunner

from Unittest.class11_suite_runner.unit_demo import UnitDemo

discover = unittest.defaultTestLoader.discover(start_dir='./', pattern='unit_report.py')
report_dir = './report/'
# 报告名称
report_file = report_dir + 'report.html'
# title
title = 'DEMO系统的测试报告'
# description
description = '本次是属于0.1版本的首轮冒烟测试执行结果'
#  判断报告路径是否存在。
if not os.path.exists(report_dir):
    os.mkdir(report_dir)
# 生成HTMLTestRunner测试报告相当于在文件中写入内容
with open(report_file, 'wb') as file:
    runner = HTMLTestRunner(stream=file, title=title,
                            description=description)
    runner.run(discover)