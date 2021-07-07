import unittest

# ddt模块的导入
from ddt import ddt, data, unpack, file_data

'''
    ddt的使用：
        1. 在需要调用ddt模块的类名处，通过装饰器的形式声明调用
        2. ddt驱动文件内容，除去Yaml之外，其他的文件都需要自行定义函数来驱动
            读写文件内容进行数据驱动其本质还是驱动的数据
        3. yaml文件是唯一一种可以和ddt模块完美搭配的文件格式，通过file_data装饰器来处理
'''


# def readFile():
#     file = open('./data/demo.txt', 'r', encoding='utf-8')
#     for line in file.readlines():
#         print(type(line))
#         print(line)


@ddt
class UnitDdt(unittest.TestCase):
    # 测试用例：都是基于函数进行管理，就意味着，可以设置形参
    '''
        在ddt的数据驱动中，如果data装饰器设置有多个值，那么就会运行多次测试用例。
        data装饰解析机制：
            @data('虚竹', '贾嫣')
            基于,来进行解析数据，获得'虚竹'和'贾嫣'两个不同的字符串，data会认为本次用例
            将会执行两次，一次传入'虚竹'，一次传入'贾嫣'
            例如登录：
                多组不同数据，执行同一个流程
            如果单次要传入多个数据，就需要对数据内容进行打包:
            例如：
                @data(['虚竹', 18], ['贾嫣', 10])
                基于,进行解析，会获得['虚竹', 18]和['贾嫣', 10]数据内容
                unpack与data的解析机制是一样的，都是依照同样的规则进行解析内容，
                只是unpack解析的是data已经解析之后的数据内容
                data解析之后确定用例的执行次数
                unpack只是将本次执行的数据进行解析
    '''

    @file_data('./data/data_dict.yaml')
    def test_01(self, **kwargs):
        print(kwargs)
        # print(age)
    # @data(*readFile())
    # def test_02(self, name):
    #     print(name)


if __name__ == '__main__':
    unittest.main()
    # readFile()
