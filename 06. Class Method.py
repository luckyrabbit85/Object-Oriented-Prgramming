# Python - Object Oriented Programming
# In here we will set a @classmethod and change the raise_amt.


class Employee:

    num_of_empls = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@Company.com'

        Employee.num_of_empls += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('Tom', 'Hanks', 50000)
emp_2 = Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.05)  # Setting the Class raise amount to 1.05

print(Employee.raise_amt)  # printing the raise amount
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print("______")  # Random just to differentiate between the results

emp_1.set_raise_amt(1.05)  # People rarely do this

print(Employee.raise_amt)  # printing the raise amount
print(emp_1.raise_amt)
print(emp_2.raise_amt)
