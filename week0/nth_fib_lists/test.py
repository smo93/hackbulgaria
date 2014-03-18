import unittest
import solution


class NthFibListsTest(unittest.TestCase):
    """docstring for NthFibListsTest"""
    def test_nth_fib_lists(self):
        self.assertEqual([1], solution.nth_fib_lists([1], [2], 1))
        self.assertEqual([2], solution.nth_fib_lists([1], [2], 2))
        self.assertEqual([1, 2, 3, 1, 2, 3],\
                solution.nth_fib_lists([], [1, 2, 3], 4))

if __name__ == '__main__':
    unittest.main()
