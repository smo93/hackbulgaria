import unittest
import solution
from subprocess import call, check_output


class Cat2Test(unittest.TestCase):
    """docstring for Cat2Test"""
    def setUp(self):
        call('echo \'File1\' > file1', shell=True)
        call('echo \'File2\' > file2', shell=True)

    def test_cat2(self):
        expexted_output = 'File1\n\nFile2\n\n'
        output = check_output('py solution.py file1 file2', shell=True)
        output = output.decode()
        self.assertEqual(expexted_output, output)

    def tearDown(self):
        call('rm file1 file2', shell=True)

if __name__ == '__main__':
    unittest.main()
