
import unittest

class UnitAaaa(unittest.TestCase):

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
    @unittest.skip('无条件跳过该条用例')
    def test_04(self):
        self.assertEqual(1, 2, msg='断言失败')

# UnitTest的运行
if __name__ == '__main__':
    unittest.main()
