class Employee:
    # these are additional class variables
    num_employ = 0
    raise_amount = 1.04

    # this is the definition of the class variables
    def __init__(self, first, last, department, pay):
        self.first = first
        self.last = last
        self.department = department
        self.pay = float(pay)
        self.email = first + '.' + last + '@company.com'

        Employee.num_employ += 1

    # method to get the full names of the employees and other stuff
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def dept(self):
        return '{}'.format(self.department)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('mark', 'mumo', 'finance', '60000')
emp_2 = Employee('liz', 'mukai', 'marketing', '100000')
emp_3 = Employee('rom', 'yula', 'sales', '400000')

emp_1.raise_amount = 1.05

emp_1.apply_raise()
print(emp_1.raise_amount)
print(emp_1.pay)

print(Employee.num_employ)