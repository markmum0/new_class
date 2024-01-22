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

    # i need the details of the employee
    def full_details(self):
        return '{} {} : {} : {} : {}'.format(self.first, self.last, self.department, self.pay, self.email)

    # method to get the full names of the employees and other stuff
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def dept(self):
        return '{}'.format(self.department)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # class methods affect all the instances in the class.
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # static methods however are not related to the class or instances at all. they can be methods that provide a different functionality
    # this is a function to determine if a date is a workday
    @staticmethod
    def work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # am using the class method as alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, department, pay = emp_str.split('+')
        return cls(first, last, department, pay)


# the new class developer inherits attributes from the employee class
class Developer(Employee):

    def __init__(self, first, last, department, pay, prog_lang):
        super().__init__(first, last, department, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, department, pay, employees=None):
        super().__init__(first, last, department, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1 = Employee('mark', 'mumo', 'finance', '60000')
emp_2 = Employee('liz', 'mukai', 'marketing', '100000')
emp_3 = Employee('rom', 'yula', 'sales', '400000')

# this changes the raise amount for all the instances in the class i.e. the entire class
# Employee.raise_amount = 1.05

# below changes the raise amount for a particular instance
# emp_1.raise amount = 1.05

# now I can use the class method to apply the raise to all employees at once
# Employee.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)

# now I am calling the work_day function in the Employee class to check whether the date was a weekday. I had to import datetime
# import datetime

# my_date = datetime.date(2024, 1, 16)
# print(Employee.work_day(my_date))

# emp = 'mar+mumo+sales+10000'
# emp_4 = Employee.from_string(emp)
# print(emp_4.fullname())

# print(Employee.num_employ)

# print(emp_4.full_details())

dev_1 = Developer('mark', 'mumo', 'soft', '150000', 'python')
# print(dev_1.email)

# print(dev_1.prog_lang)
# dev_1.apply_raise()
# print(dev_1.pay)

mngr_1 = Manager('jan', 'smith', 'acquisitions', '90000', [dev_1])

mngr_1.add_emp(emp_1)

mngr_1.print_employees()