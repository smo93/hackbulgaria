import unittest
import manage_company
import sqlite3
from subprocess import call


class ManageCompanyTest(unittest.TestCase):
    """docstring for ManageCompanyTest"""
    def setUp(self):
        call('py create_company.py', shell=True)

        self.conn = sqlite3.connect('hackbulgaria.db')
        self.cursor = self.conn.cursor()


    def test_list_employees(self):
        expected = '1 - Ivan Ivanov - Software Developer\n'\
                    '2 - Rado Rado - Technical Support Intern\n'\
                    '3 - Ivo Ivo - CEO\n'\
                    '4 - Petar Petrov - Marketing Manager\n'\
                    '5 - Maria Georgieva - COO\n'
        self.assertEqual(expected, manage_company.list_employees(self.cursor))

    def test_monthly_spending(self):
        expected = 'The company is spending $26500 every month!'
        self.assertEqual(expected, manage_company.monthly_spending(self.cursor))

    def test_yearly_spending(self):
        expected = 'The company is spending $121000 every year!'
        self.assertEqual(expected, manage_company.yearly_spending(self.cursor))

    def test_add_employee(self):
        manage_company.add_employee(self.cursor, 'Asd Dsa', 10, 0, 'Sanitation Worker')

        sql_add = 'SELECT * FROM employees WHERE name=\'Asd Dsa\''
        sql_result = self.cursor.execute(sql_add).fetchone()

        self.assertEqual('Asd Dsa', sql_result[1])
        self.assertEqual(10, sql_result[2])
        self.assertEqual(0, sql_result[3])
        self.assertEqual('Sanitation Worker', sql_result[4])

        sql_del = 'DELETE FROM employees WHERE name=\'Asd Dsa\''
        self.cursor.execute(sql_del)

    def test_delete_employee(self):
        manage_company.delete_employee(self.cursor, 5)

        expected = '1 - Ivan Ivanov - Software Developer\n'\
                    '2 - Rado Rado - Technical Support Intern\n'\
                    '3 - Ivo Ivo - CEO\n'\
                    '4 - Petar Petrov - Marketing Manager\n'
        self.assertEqual(expected, manage_company.list_employees(self.cursor))

        manage_company.add_employee(self.cursor, 'Maria Georgieva', 8000, 10000, 'COO')

    def test_update_employee(self):
        manage_company.update_employee(self.cursor, 1, 'Asd Dsa', 10, 0,
            'Sanitation Worker')

        expected = '1 - Asd Dsa - Sanitation Worker\n'\
                    '2 - Rado Rado - Technical Support Intern\n'\
                    '3 - Ivo Ivo - CEO\n'\
                    '4 - Petar Petrov - Marketing Manager\n'\
                    '5 - Maria Georgieva - COO\n'
        self.assertEqual(expected, manage_company.list_employees(self.cursor))

    def tearDown(self):
        self.conn.close()
        call('rm hackbulgaria.db', shell=True)

if __name__ == '__main__':
    unittest.main()
