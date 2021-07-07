import yaml
from ddt import ddt, data, unpack, file_data
import unittest

# file=open('./data/test_data1.yaml', mode='r',encoding='utf-8')
# data = yaml.load(stream=file, Loader=yaml.FullLoader)
# print(data)
test_data1 = [{"username": "zhangsan", "pwd": "zhangsan"},
              {"username": "lisi", "pwd": "lisi"},
              {"username": "wangwu", "pwd": "wangwu"},
              ]
test_data2 = [{"username": "wukong", "pwd": "wukong"},
              {"username": "wuneng", "pwd": "woneng"},
              {"username": "wujing", "pwd": "wujing"},
              ]

@ddt
class Test(unittest.TestCase):
    def setUp(self):
        print("===Start!===")
    def tearDown(self):
        print("===end!===")
    @data(*test_data1)
    def test_ddt1(self, data):
        print(data)
    # ```
    # test_ddt1的测试结果是OK的，因为test_data2作为一个整体传给了data,所以value打印的值为test_data1
    # ```

    @data(*test_data2)
    def test_ddt2(self, data):
        print(data['username'])
    # ```
    # test_ddt2的测试结果是OK的，因为test_data2作为一个整体传给了data,然后根据字典取出value值
    # ```

    @data([3,2,1],[5,3,2],[10,4,6])
    # @unpack #@unpack，那么[3,2,1]被分解开，按照用例中的三个参数传递
    def test_minus(self,a,b,expected):
        actual = int(a)-int(b)
        expected = int(expected)
        print(actual,expected)
        self.assertEqual(actual, expected)

    # test_minus的测试结果也是ok的，由于在 @ data(...)下加了 @ unpack, 代表会把数据分解，得到3组测试数据
    #

    @data([2, 3], [4, 5]) #没有@unpack，那么[2,3]当成一个参数传入用例运行
    def test_compare(self, a, b):
        print(a,b)
        self.assertEqual(a, b)
    # ```
    # test_compare的测试结果是fail的，由于没有加 @ unpack, 虽然还是会被理解成2组测试数据，但是[2, 3]
    # 作为一个整体被传给了a, 因为b就没有值传入了，所以一执行后报了
    # TypeError: test_compare() missing 1 required positional argument: 'b' 这句错
    # ```
if __name__ == "__main__":
    unittest.main()