import unittest
import solution

class IsNumberBalancedTest(unittest.TestCase):
    """docstring for IsNumberBalancedTest"""
    def test_is_number_balanced(self):
        self.assertTrue(solution.is_number_balanced(4518))
        self.assertTrue(solution.is_number_balanced(1238033))
        self.assertFalse(solution.is_number_balanced(28471))

if __name__ == '__main__':
    unittest.main()
