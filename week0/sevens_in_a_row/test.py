import unittest
import solution


class SevensInARowTest(unittest.TestCase):
    """docstring for SevensInARowTest"""
    def test_sevens_in_a_row(self):
        self.assertTrue(solution.sevens_in_a_row([7, 7, 7], 3))
        self.assertFalse(solution.sevens_in_a_row([7, 7, 7], 4))
        self.assertTrue(solution.sevens_in_a_row([1, 2, 7, 7, 7, 3, 7, 9], 3))
        self.assertTrue(solution.sevens_in_a_row([1, 2, 9], 0))

if __name__ == '__main__':
    unittest.main()
