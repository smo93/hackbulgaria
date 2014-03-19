import unittest
import solution


class ReduceFilePathTest(unittest.TestCase):
    """docstring for ReduceFilePathTest"""
    def test_reduce_file_path(self):
        self.assertEqual('/', solution.reduce_file_path('.././'))
        self.assertEqual('/home/asd',\
                solution.reduce_file_path('/home/sad/.././asd/'))
        self.assertEqual('/', solution.reduce_file_path('////'))

if __name__ == '__main__':
    unittest.main()
