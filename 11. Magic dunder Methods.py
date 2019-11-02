# Python - Object Oriented Programming
# In here we will use special methods, also called as Magic methods.
# Double underscore is called as dunder. we have seen dunder __init__ fuction
# we will see __repr__ and __str__ in here.
# __repr__ is meant to be unambiguous representation of the object and can be
# used for debugging by the developers
# __str__ is meant to be more readable implementation of the object meant to be
# read by the user.
# Then we will see custom dunder that we can create for performing certain
# function.


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

    def __repr__(self):  # copy and paste seomthing which returns the same obj
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Tom', 'Hanks', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)  # __str__ preferred over __repr__ if both present

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

print(emp_1 + emp_2)  # Gives us combined salary for emp_1 and emp_2
print(len(emp_1))
