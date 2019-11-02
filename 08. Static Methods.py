# Python - Object Oriented Programming
# We have seen that Regular method automatically pass the instance as arguments
# self, Class method automatically pass the class as aurgument cls, Static
# method dont pass anything automatically. so they behave like regular function
# except we include them in classe because they have seom logical connection
# with the class.
import datetime


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

    @classmethod  # classmethod, aka Decotators
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod  # Constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # staticmethod
    def is_workday(day):  # not instance, nor Class. Taking argument as day
        if day.weekday() == 5 or day.weekday() == 6:  # Mon = 0, Sun = 6
            return False
        return True


emp_1 = Employee('Tom', 'Hanks', 50000)
emp_2 = Employee('Test', 'User', 60000)

# checking a day is working day or not
my_date = datetime.date(2019, 11, 2)

print(Employee.is_workday(my_date))
