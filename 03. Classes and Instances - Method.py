# Python - Object Oriented Programming
# Lets look at creating a method onto a Class


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@Company.com'

    def fullname(self):  # Here we created a method named fullname on our class
        return f'{self.first} {self.last}'


emp_1 = Employee('Tom', 'Hanks', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Printing Employee full name. Notice the '()' in the end. This is because we
# are calling a method not an attribute.
print(emp_1.fullname())
print(emp_2.fullname())

# Note : Without parenthesis it will return the method not the values.

# we can also run these methods using class name itself
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
