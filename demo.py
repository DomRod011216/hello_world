#testing database
import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')

c = conn.cursor()

#using To create strings that span multiple lines, triple single quotes
#''' or triple double quotes """ are used to enclose the string.
# ''' This string is on multiple lines within three single quotes
# on either side. ''' """ This string is on multiple lines within
# three double quotes on either side.

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first and last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first = :first and last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 800000)
emp_2 = Employee('Jane', 'Doe', 900000)

#testing funtions

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)





conn.close()


# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
#
# conn.commit()
#
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
#
# conn.commit()

# c.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))
#
# print(c.fetchall())
#
# c.execute("SELECT * FROM employees WHERE last=:last", ({'last': 'Doe'}))
#
# print(c.fetchall())