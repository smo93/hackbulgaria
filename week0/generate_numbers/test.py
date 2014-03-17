import unittest
import solution
from subprocess import call


class GenerateNumbersTest(unittest.TestCase):
    """docstring for GenerateNumbersTest"""
    def setUp(self):
        call('py solution.py rand.txt 100', shell=True)

    def test_generate_numbers(self):
        rand_file = open('rand.txt', 'r')
        integers = rand_file.read().split(' ')
        integers = [int(x) for x in integers]
        rand_file.close()

        self.assertEqual(100, len(integers))

        integers = sorted(integers)
        self.assertTrue(0 < integers[0])
        self.assertTrue(1000 > integers[-1])

    def tearDown(self):
        call('rm rand.txt', shell=True)

if __name__ == '__main__':
    unittest.main()

