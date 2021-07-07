'''
    UnitTest中的skip装饰器应用:
        总计四种不同的skip装饰器：
            1. @unittest.skip：用例执行时，无条件跳过该条用例
            2. @unittest.skipIf：当if条件为真时，执行跳过操作
            3. @unittest.skipUnless：与skipIf相反，当条件为假时，执行跳过操作
            4. @unittest.expectedFailure：当用例报错的时候，系统选择忽略
'''
# 导入UnitTest环境
import unittest



# UnitTest类对象
class UnitDemo(unittest.TestCase):

    # 测试用例2
    # @unittest.skipIf(temp is None, '跳过if')
    def test_02(self):
        print('02')

    # 测试用例1
    # @unittest.skip('无条件跳过该条用例')
    def test_01(self):
        print('01')

    # 测试用例03
    # @unittest.skipUnless(1 == 1, '跳过unless')
    def test_03(self):
        print('03')

    # 测试用例04
    # @unittest.expectedFailure
    def test_04(self):
        self.assertEqual(1, 2, msg='断言失败')

# UnitTest的运行
if __name__ == '__main__':
    unittest.main()
