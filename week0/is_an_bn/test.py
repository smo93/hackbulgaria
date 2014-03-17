import unittest
import solution


class IsAnBnTest(unittest.TestCase):
    """docstring for IsAnBnTest"""
    def test_is_an_bn(self):
        self.assertTrue(solution.is_an_bn(''))
        self.assertTrue(solution.is_an_bn('aabb'))
        self.assertFalse(solution.is_an_bn('aaabb'))

if __name__ == '__main__':
    unittest.main()
