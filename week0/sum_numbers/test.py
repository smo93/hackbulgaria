import unittest
from sum_numbers import sum_ints_from_file
from subprocess import call


class SumIntsFromFileTest(unittest.TestCase):
    """docstring for SumIntsFromFileTest"""
    def test_sum_ints_from_file(self):
        call('echo \'15 10 25 30\' > test_file.txt', shell=True)
        self.assertEqual(80, sum_ints_from_file('test_file.txt'))
        call('rm test_file.txt', shell=True)

if __name__ == '__main__':
    unittest.main()
