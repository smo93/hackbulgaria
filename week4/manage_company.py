import sqlite3


def list_employees(curosr):
    sql = 'SELECT id, name, position FROM employees'
    sql_result = curosr.execute(sql).fetchall()

    result = []

    for row in sql_result:
        result.append('{0} - {1} - {2}'.format(row[0], row[1], row[2]))

    return '\n'.join(result) + '\n'

def monthly_spending(cursor):
    sql = 'SELECT monthly_salary FROM employees'
    sql_result = cursor.execute(sql).fetchall()

    sum = 0

    for row in sql_result:
        sum += row[0]

    return 'The company is spending ${} every month!'.format(sum)

def yearly_spending(cursor):
    sql = 'SELECT yearly_bonus FROM employees'
    sql_result = cursor.execute(sql).fetchall()

    sum = 0

    for row in sql_result:
        sum += row[0]

    return 'The company is spending ${} every year!'.format(sum)

def add_employee(cursor, name, monthly_salary, yearly_bonus, position):
    employee_id = cursor.lastrowid

    sql = 'INSERT INTO employees VALUES(?, ?, ?, ?, ?)'
    sql_result = cursor.execute(sql, (employee_id,\
            name, monthly_salary, yearly_bonus, position)).fetchone()

def delete_employee(cursor, employee_id):
    sql = 'DELETE FROM employees WHERE id=?'
    cursor.execute(sql, (employee_id, ))

def update_employee(cursor, employee_id, name, monthly_salary, yearly_bonus, position):
    sql = 'UPDATE employees SET name=?, monthly_salary=?, yearly_bonus=?,'\
        'position=? WHERE id=?'
    cursor.execute(sql, (name, monthly_salary, yearly_bonus, position, employee_id))
