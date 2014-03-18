import unittest
import solution
import os
from time import time
from datetime import datetime
from subprocess import call


class PizzaaTest(unittest.TestCase):
    """docstring for PizzaaTest"""
    def setUp(self):
        pass

    def test_take_order(self):
        orders = {}
        solution.add_order(orders, 'Az', 10.0)
        self.assertEqual({'Az': 10.0}, orders)
        solution.add_order(orders, 'Az', 10.0)
        self.assertEqual({'Az': 20.0}, orders)

    def test_status(self):
        orders = {'Az': 10.0,
                'Ti': 20.0}
        expected = 'Az - 10.0\nTi - 20.0\n'
        self.assertEqual(expected, solution.print_status(orders))

    def test_save(self):
        orders = {'Az': 10.0,
                'Ti': 20.0}
        solution.save(orders)
        ts = time()
        stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
        save_filename = 'orders_' + stamp
        self.assertTrue(os.path.isfile(save_filename))
        saved_file = open(save_filename, 'r')
        content = '\n'.join(sorted(saved_file.read().splitlines()))
        saved_file.close()
        expected = 'Az - 10.0\nTi - 20.0'
        self.assertEqual(expected, content)
        os.remove(save_filename)

    def test_list(self):
        call('touch orders_2014_03_18_13_58_39', shell=True)
        call('touch orders_2014_03_18_13_58_49', shell=True)
        expected = {1: 'orders_2014_03_18_13_58_39',
                2: 'orders_2014_03_18_13_58_49'}
        self.assertEqual(expected, solution.list_order_files())
        call('rm orders_*', shell=True)

    def test_load(self):
        file = open('orders_2014_03_18_13_58_49', 'w')
        file.write('Az - 10.0')
        file.close()

        dict_of_orders = solution.list_order_files()
        orders = {}
        solution.load_orders(1, dict_of_orders, orders)
        self.assertEqual({'Az': 10.0}, orders)
        call('rm orders_2014_03_18_13_58_49', shell=True)

if __name__ == '__main__':
    unittest.main()
