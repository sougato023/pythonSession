# # Classes
# # In object-oriented programming you
# # write classes that represent real-world things
# # and situations, and you create objects based on these
# # classes. When you write a class, you define the general
# # behavior that a whole category of objects can have.

# class Dog():
#     """A simple attempt to model a dog."""
    
#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         print("I am in init method")
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(self.name.title() + " is now sitting.")

#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(self.name.title() + " rolled over!")

# # #Creating instance of a class
# # my_dog = Dog('willie', 6)
# # print("My dog's name is " + my_dog.name.title() + ".")
# # print("My dog is " + str(my_dog.age) + " years old.")

# # #calling methods
# # my_dog = Dog('willie', 6)
# # my_dog.sit()
# # my_dog.roll_over()

# # multiple instances
# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
# my_dog.sit()
# print("\nYour dog's name is " + your_dog.name.title() + ".")
# print("Your dog is " + str(your_dog.age) + " years old.")
# your_dog.roll_over()

# # Working with classes and instances
# class Car():
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

# #  Setting default values for an attribute
# class Car():
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# #Modifying an attrbutes value directly
# class Car():
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# # Modifying an attribute value through a method
# class Car():
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")

#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         self.odometer_reading = mileage

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.update_odometer(33)
# my_new_car.read_odometer()

# Modifying an attribute value through a method
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(33)
my_new_car.read_odometer()

