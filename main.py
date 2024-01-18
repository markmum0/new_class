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


emp_1 = Employee('mark', 'mumo', 'finance', '60000')
emp_2 = Employee('liz', 'mukai', 'marketing', '100000')
emp_3 = Employee('rom', 'yula', 'sales', '400000')

# this changes the raise amount for all the instances in the class i.e. the entire class
# Employee.raise_amount = 1.05

# below changes the raise amount for a particular instance
# emp_1.raise amount = 1.05

# now I can use the class method to apply the raise to all employees at once
Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)

# now I am calling the work_day function in the Employee class to check whether the date was a weekday. I had to import datetime
import datetime

my_date = datetime.date(2024, 1, 16)
print(Employee.work_day(my_date))
