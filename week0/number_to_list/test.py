import unittest
import solution


class NumberToListTest(unittest.TestCase):
    """docstring for NumberToListTest"""
    def test_number_to_list(self):
        self.assertEqual([1, 2, 3], solution.number_to_list(123))
        self.assertEqual([1, 2, 3, 0, 2, 3], solution.number_to_list(123023))

if __name__ == '__main__':
    unittest.main()
