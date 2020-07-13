# Python - Object Oriented Programming
# Class variables are variables that are shared among all instances in the
# class. Instance variables can be unique for each instances line name, email
# and pay.


class Employee:

    raise_amt = 1.04  # Class Vaiable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@Company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # In the above line we can use Employee.raise_amt as well as self.raise_amt
    # depending on our interest but not raise_amt.


emp_1 = Employee('Tom', 'Hanks', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)  # printing the pay after raise.

print(Employee.raise_amt)  # printing the raise amount
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# As we can see we can access the class variable from both the class and
# the instance. As we try to acess an attribute on an instance, it first's
# checks whether the instance has that attribute or not, then it will see the
# class or any class that inherits from contains that attribute.

print(emp_1.__dict__)  # raise_amt is not present
print(Employee.__dict__)  # raise_amt is present

# Increasing the raise amount of emp_1 from instance and using
# self.raise_amt in the method.
emp_1.raise_amt = 1.05

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)


# Here we can see if we use self.raise_amt we can individually raise the
# amount of each employee by using that instance and raise_amt. Also using
# self here will allow any subclass to overwrite the constant if they wanted to
# Lets see another example where we don't want to use self in the next section
