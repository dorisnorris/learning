import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees(
			first text,
			last text,
			pay integer
			)""")

def insert_emp(empl):
	with conn:
		c.execute("INSERT INTO employees VALUES(:first, :last, :pay)", {'first': empl.first, 'last': empl.last, 'pay': empl.pay})

def get_empls_by_name(lastname):
	c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
	return c.fetchall()

def update_pay(empl, pay):
	with conn:
		c.execute("""UPDATE employees SET pay = :pay
					WHERE first = :first AND last = :last""",
					{'first': empl.first, 'last': empl.last, 'pay': pay})

def remove_emp(empl):
	with conn:
		c.execute("DELETE from employees WHERE first = :first AND last = :last",
			{'first': empl.first, 'last': empl.last})

empl_1 = Employee('John', 'Doe', 80000)
empl_2 = Employee('Jane', 'Doe', 90000)

insert_emp(empl_1)
insert_emp(empl_2)

empls = get_empls_by_name('Doe')
print(empls)

update_pay(empl_2, 95000)
remove_emp(empl_1)

empls = get_empls_by_name('Doe')
print(empls)


# c.execute("INSERT INTO employees VALUES(?, ?, ?)", (empl_1.first, empl_1.last, empl_1.pay))

# conn.commit()

# c.execute("INSERT INTO employees VALUES(:first, :last, :pay)", {'first': empl_2.first, 'last': empl_2.last, 'pay': empl_2.pay})

# conn.commit()


# c.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))

# print(c.fetchall())

# c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})

# print(c.fetchall())

# conn.commit()

conn.close()
