import unittest
from subprocess import call


class spacifyTest(unittest.TestCase):

    def setUp(self):
        self.filename = 'test'
        self.file_handle = open(self.filename, 'w')

    def test_spacify(self):
        self.file_handle.write('\tasd')
        self.file_handle.close()

        call('py spacify.py test', shell=True)

        f = open(self.filename, 'r')
        content = f.read()
        f.close()

        self.assertEqual('    asd', content)

    def tearDown(self):
        call(['rm test')

if __name__ == '__main__':
    unittest.main()
