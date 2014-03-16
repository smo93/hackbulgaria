import unittest
import solution
from subprocess import check_output
import os


class CatTest(unittest.TestCase):
    """docstring for CatTest"""
    def setUp(self):
        self.filename = 'test.txt'
        test_file = open(self.filename, 'w')
        test_file.write('This is some file.')
        test_file.close()

    def test_cat(self):
        output = check_output(['py', 'solution.py', self.filename]).decode()
        self.assertEqual('This is some file.\n', output)

    def tearDown(self):
        os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()
