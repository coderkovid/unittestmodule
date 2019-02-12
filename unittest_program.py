import unittest
from employee import Employee

class TestClass(unittest.TestCase):
	def test_email(self):
		emp1 = Employee('Kovid', 'Panthy', 5000)
		emp2 = Employee('John', 'Wales', 2000)

		self.assertEqual(emp1.email(), 'Kovid.Panthy@coderkovid.com')
		self.assertEqual(emp2.email(), 'John.Wales@coderkovid.com')

	def test_i_wage(self):
		emp1 = Employee('Kovid', 'Panthy', 5000)
		emp2 = Employee('John', 'Wales', 2000)

		self.assertEqual(emp1.increase_wage(), 'New wage = 5250')
		self.assertEqual(emp2.increase_wage(), 'New wage = 2100')

if __name__ == '__main__':
	unittest.main()