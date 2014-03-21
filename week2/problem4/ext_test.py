import unittest
from subprocess import call, check_output


class extTest(unittest.TestCase):

    def setUp(self):
        call('mkdir test_dir', shell=True)
        for i in range(5):
            call('touch test_dir/%d.cpp' % (i), shell=True)
        for i in range(3):
            call('touch test_dir/%d.h' % (i), shell=True)

    def test_ext_with_cpp(self):
        result = check_output('py ext.py test_dir/ .cpp', shell=True).decode()
        result = int(result)
        self.assertEqual(5, result)

    def test_ext_with_h(self):
        result = check_output('py ext.py test_dir/ .h', shell=True).decode()
        result = int(result)
        self.assertEqual(3, result)

    def test_ext_with_no_extension(self):
        result = check_output('py ext.py test_dir/ py', shell=True).decode()
        result = int(result)
        self.assertEqual(0, result)

    def tearDown(self):
        call('rm -r test_dir/', shell=True)

if __name__ == '__main__':
    unittest.main()
