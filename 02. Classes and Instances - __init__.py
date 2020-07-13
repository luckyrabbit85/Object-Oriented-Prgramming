# Python - Object Oriented Programming
# Lets look at the __inti__ method


class Employee:  # This is our class named Employee

    # When we create methods within a Class they recieve the instances as
    # the first argument. By convention we should call the instance 'self'
    # (not compulsory but it's good to follow conventions). After 'self' we
    # pass on the arguments.

    def __init__(self, first, last, pay):  # Initialize or (Constructor)
        self.first = first  # It can also be self.fname or any name
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@Company.com'

# Now we create instances of our Employee class and pass on values that we
# specified in our __init__ method. The __init__ method takes the instance
# called 'self' and other arguments. When we create instances 'self' passed on
# automatically so we can leave off self and provide names and pay
# emp_1 and emp_2 are passes on as self in the initialize and then instance
# attributes are created.


emp_1 = Employee('Tom', 'Hanks', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)  # Printing out instances attributes
print(emp_2.email)

print(f'{emp_1.first} {emp_1.last}')  # Printing Employee full name

# Thats too much of typing to get full name, instead in the next section we
# will se a 'method' build on our class to do that.
