# Python - Object Oriented Programming
# Raise can be different for different employees or instances.
# But total number of employees will not be different for any instance.
# so lets create a class variable names num_of employees.


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@Company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp_1 = Employee('Tom', 'Hanks', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)

# Next we will see Class Methods ans Static Methods
