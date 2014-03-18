import unittest
import solution


class MagicSqareTest(unittest.TestCase):
    """docstring for MagicSqareTest"""
    def test_magic_sqare(self):
        self.assertFalse(solution.magic_square([[1,2,3], [4,5,6], [7,8,9]]))
        self.assertTrue(solution.magic_square([[4,9,2], [3,5,7], [8,1,6]]))

if __name__ == '__main__':
    unittest.main()
