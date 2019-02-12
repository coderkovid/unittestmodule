class Employee:
	percentage = 0.05
	def __init__(self, f_name, l_name, wage):
		self.f_name = f_name
		self.l_name = l_name
		self.wage = wage

	def email(self):
		return '{}.{}@coderkovid.com'.format(self.f_name, self.l_name)

	def increase_wage(self):
		self.wage = self.wage * self.percentage + self.wage
		return 'New wage = {}'.format(int(self.wage))
