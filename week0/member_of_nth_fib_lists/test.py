import unittest
from solution import member_of_nth_fib_lists


class MemberOfNthFibListTest(unittest.TestCase):
    """docstring for MemberOfNthFibListTest"""
    def test_member_of_nth_fib_list(self):
        self.assertFalse(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
        self.assertFalse(member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]))
        self.assertTrue(member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]))

if __name__ == '__main__':
    unittest.main()
