import unittest
import solution


class IsIncreasingTest(unittest.TestCase):
    """docstring for IsIncreasingTest"""
    def test_is_increasing(self):
        self.assertTrue(solution.is_increasing([1,2,3,4,5]))
        self.assertTrue(solution.is_increasing([1]))
        self.assertFalse(solution.is_increasing([1,1,1,1]))

if __name__ == '__main__':
    unittest.main()
