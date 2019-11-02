# Python - Object Oriented Programming
# Sometimes we need to initiate our subclasses with more information than our
# parent class can handle. Lets say we want to pass on main programming lang
# as an attribute but currently our Employee Class accepts only 3 attributes
# namely first, last and pay


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


class Developer(Employee):  # Will only handle prog_lang and rest by Employee
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # Alternate to this below
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manger(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
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

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Tom', 'Hanks', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manger('Susan', 'Smith', 90000, [dev_1])

print(dev_1.email)
print(dev_1.prog_lang)

print(mgr_1.email)
print(mgr_1.print_emps())

mgr_1.add_emp(dev_2)
print(mgr_1.print_emps())

mgr_1.remove_emp(dev_1)
print(mgr_1.print_emps())

print('_____________')
# Is instance function

print(isinstance(mgr_1, Manger))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print('____________')

# Is subclasses function

print(issubclass(Developer, Employee))
print(issubclass(Manger, Employee))
print(issubclass(Manger, Developer))
