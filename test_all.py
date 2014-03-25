from glob import glob
from subprocess import check_output
import unittest


tests_filenames = glob('*/test.py')
#tests_filenames = check_output('find ./ -name test.py', shell=True).decode().splitlines()
modules = [str[:-3].split('/') for str in tests_filenames]
suites = [unittest.defaultTestLoader.loadTestsFromName(str)\
        for str in modules]
testSuite = unittest.TestSuite(suites)
text_runner = unittest.TextTestRunner().run(testSuite)
