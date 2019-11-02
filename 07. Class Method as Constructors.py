# Python - Object Oriented Programming
# In here we will set a @classmethod as a constructor


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

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee('Tom', 'Hanks', 50000)
emp_2 = Employee('Test', 'User', 60000)

'''Class methods as alternative constructors'''

emp_str_1 = 'John-Woo-70000'
emp_str_2 = 'steve-Jobs-80000'
emp_str_3 = 'Mary-Jane-30000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
