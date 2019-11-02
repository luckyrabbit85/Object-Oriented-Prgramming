# Python - Object Oriented Programming
# Inheritance allows us to inherit attributes and methods from a parent class
# This is useful because we can create subclasses and get all of the
# functionality of parent class and then we can add or overwrite completely new
# functionality without effecting the parent class.


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@Company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):  # Creating a new subclass from Employee Class
    raise_amt = 1.10  # Adding raise amount to subclass


dev_1 = Developer('Tom', 'Hanks', 50000)  # creating new developers
dev_2 = Developer('Test', 'User', 60000)

# print(help(Developer))  # Check out the Method resolution order

# print(dev_1.email)
# print(dev_2.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
