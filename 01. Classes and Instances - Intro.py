# Python - Object Oriented Programming
# In this script we will define a simple - Class, Instance and
# Instance attributes


class Employee:  # This is our class named Employee
    pass


emp_1 = Employee()  # These are instances of our class, namely emp_1 and emp_2
emp_2 = Employee()

print(emp_1)  # Printing out instances
print(emp_2)

emp_1.first = 'Tom'  # These are attributes of our instance emp_1
emp_1.last = 'Hanks'
emp_1.email = 'Tom.Hanks@Company.com'
emp_1.pay = 50000

emp_2.first = 'Test'  # These are attributes of our instance emp_2
emp_2.last = 'User'
emp_2.email = 'Test.User@Company.com'
emp_2.pay = 60000

print(emp_1.email)  # Printing out instances attributes
print(emp_2.email)

#  This way of creating instances attributes manually is of no help so we will
#  look another method called __init__ in the next section.
