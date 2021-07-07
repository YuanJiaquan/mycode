import unittest

'''
    Skip装饰器，通过@unittest.skip进行调用
        总计有四种不同的skip装饰器：
            1. @unittest.skip：无条件跳过该用例执行
            2. @unittest.skipif：当if条件为真时，跳过
            3. @unittest.skipUnless：与skipif相反，当条件为假的时候，跳过
            4. @unittest.expectedFailure：当用例报错时，系统选择忽略
'''


class Demo(unittest.TestCase):
    # @unittest.skipIf(1 == 1, '1 == 1 的条件')
    def test_2(self):
        print('test 2')

    # @unittest.skip('这是一个skip装饰器')
    def test_1(self):
        print('test 1')

    # @unittest.skipUnless(1 == 2, '1 == 2 的条件')
    def test_3(self):
        print('test 3')

    # @unittest.expectedFailure
    def test_4(self):
        a = 1 / 0
        print('test 4')


if __name__ == '__main__':
    unittest.main()
