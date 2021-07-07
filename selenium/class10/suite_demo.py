'''
    UnitTest中一大特色：测试套件与测试运行器
        测试套件：可以理解为一个list集合
        默认在框架中所有的用例都会全部执行，且是依照UnitTest的规则来进行排序执行的
        例如：
            冒烟测试
            针对特定流程来执行测试
        应用一定是结合UnitTest测试框架来执行的
    套件的运行是一定需要通过运行器来进行运行操作，默认的运行器TextTestRunne
    运行套件时，用例的顺序是基于套件在添加用例时的顺序来定的。
    测试运行器：支持外部的第三方运行器，比如HTMLTestRunner
    HTML模块无法通过pip进行安装，本身是针对2版本的python来进行实现的
'''
import os
import unittest
from HTMLTestRunner import HTMLTestRunner
from HTMLTestReportCN import HTMLTestRunner

# 添加用例到套件执行
# 创建套件
suite = unittest.TestSuite()
# 1.添加用例到套件中:添加单个测试用例，通过用例的名称进行添加
# suite.addTest(Demo('test_3'))
# suite.addTest(Demo('test_2'))
# suite.addTest(Demo('test_4'))
# 2.批量添加用例到套件：一次性添加多个测试用例，通过用例集合来进行添加
# cases = [Demo('test_3'), Demo('test_2'), Demo('test_1')]
# suite.addTests(cases)
# 3.批量添加测试用例:通过TestCase对象直接添加一整个UnitTest类
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Demo))
# 4. 批量添加：通过类名来进行添加
# suite.addTests(unittest.TestLoader().loadTestsFromName('unit_skip_demo.Demo'))
# 5. 批量添加：通过文件名来进行添加
# 定义获取用例的路径
case_dir = '../'
# 基于路径来用例，组合成套件
discover = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='u*.py')
# 运行套件
# runner = unittest.TextTestRunner()
# runner.run(discover)
# 运行HTMLTestRunner生成测试报告
# 保存路径
report_path = './report/'
# 报告的文件名称
report_file = report_path + 'report3.html'
# 判断保存路径是否存在
if not os.path.exists(report_path):
    os.mkdir(report_path)
with open(report_file, 'wb') as file:
    runner = HTMLTestRunner(stream=file, title='这是第一份测试报告',
                            description='这是测试报告的描述', tester='虚竹')
    runner.run(discover)
