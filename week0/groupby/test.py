import unittest
import solution

class GroupbyTest(unittest.TestCase):
    """docstring for GroupbyTest"""
    def test_groupbu(self):
        expected = {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}
        self.assertEqual(expected,\
                solution.groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))
        expected = {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
        self.assertEqual(expected,\
                solution.groupby(lambda x: 'odd' if x % 2 else 'even',\
                [1, 2, 3, 5, 8, 9, 10, 12]))

if __name__ == '__main__':
    unittest.main()
