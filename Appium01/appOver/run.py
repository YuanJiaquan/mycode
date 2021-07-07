import HTMLTestRunner
import unittest

# discover(目录文件，执行的文件)
dict_dir='./test_case'
# 找用例文件
discover=unittest.defaultTestLoader.discover(dict_dir,'test_login.py')

with open('./reports/report1.html','wb')as f:
    HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2).run(discover)

# 文件目录 不要写死了  os.path

# 想要直接运行测试报告，需要把项目中文件配置目录，例如日志文件，配置文件路径改好
