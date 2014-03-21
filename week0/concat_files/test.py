import unittest
import solution
from subprocess import call


class ConcatTest(unittest.TestCase):
    """docstring for ConcatTest"""
    def setUp(self):
        call('echo \'File1\' > file1', shell=True)
        call('echo \'File2\' > file2', shell=True)

    def test_concat(self):
        expected_output = 'File1\n\nFile2\n\n'
        call('py solution.py file1 file2', shell=True)
        target_file = open('MEGATRON', 'r')
        output = target_file.read()
        target_file.close()
        self.assertEqual(expected_output, output)

    def tearDown(self):
        call('rm file1 file2 MEGATRON', shell=True)

if __name__ == '__main__':
    unittest.main()
