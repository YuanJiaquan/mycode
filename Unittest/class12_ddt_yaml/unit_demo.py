'''
    UnitTest中的ddt数据驱动应用:
        环境部署：
            pip install ddt
        ddt模块所有的内容都是基于装饰器的形态来实现补充的。
        一定要在调用ddt的类中声明ddt的调用，也就是在class前加入@ddt
        在需要调用数据驱动的用例前，调用@data，实现数据的驱动分离
        file_data用于处理yaml格式的文件
        yaml格式的数据驱动管理是一个yaml对应一条用例。
'''
# 导入UnitTest环境
import unittest
from ddt import ddt, data, unpack, file_data
from web_keys import WebKey


# 文件的内容读取
def read_file():
    li = []
    file = open('./data/data.txt', 'r', encoding='utf-8')
    for line in file.readlines():
        li.append(line)
    return li


# UnitTest类对象
@ddt  # 声明该class类将要调用ddt模块进行数据管理。
class UnitDemo(unittest.TestCase):
    # 预置函数
    def setUp(self) -> None:
        self.wk = WebKey('Chrome')

    # 后置函数
    def tearDown(self) -> None:
        self.wk.quit()

    # 测试用例
    '''
        data执行的操作就是拆包
            @data('虚竹', '做人嘛，最重要的就是开心', '狐狸是个留级生')
            将所有的数据以逗号进行分割：
                虚竹
                做人
                狐狸
            基于拆分出来的结果总数，定义循环次数，每次循环都传入一个参数进去
            ('http://www.jd.com', '虚竹') = *args
        当需要传入多个参数的时候，所以需要unpack进行二次解包，参数的顺序与用例入参的顺序要保持一致，参数数量要相同
        元组、list、dict都可以作为参数的传入类型
    '''

    # @data({'url': 'http://www.jd.com', 'name': 'XUZHU儿'})
    # @unpack
    # def test_01(self, url, name):
    #     self.wk.visit(url)
    #     self.wk.input('id', 'key', name)
    #     self.wk.click('xpath', '//button[@aria-label="搜索"]')
    #     self.wk.sleep(3)

    # 基于文件的内容读取，实现数据驱动: 本质意义上是调用的函数的返回值，进行操作，而文件操作本身是在函数中进行的。
    # @data(*read_file())
    # def test_02(self, name):
    #     print(name)
    #
    # def test_03(self):
    #     li = read_file()
    #     print(li)

    #  测试用例
    '''
        通过file_data读取的所有内容，传入kwargs参数
    '''

    @file_data('./data/test_data.yaml')
    def test_01(self, **kwargs):
        self.wk.visit(kwargs['url'])
        self.wk.input(**kwargs['input'])
        # self.wk.input(kwargs['input']['name'], kwargs['input']['value'], kwargs['input']['txt'])
        self.wk.click(**kwargs['click'])
        self.wk.sleep(3)

    # @file_data('./data/test_data1.yaml')
    # def test_01(self, url, txt):
    #     self.wk.visit(url)
    #     self.wk.input('id', 'key', txt)
    #     self.wk.click('xpath', '//button[@aria-label="搜索"]')
    #     self.wk.sleep(3)


# UnitTest的运行
if __name__ == '__main__':
    unittest.main()
