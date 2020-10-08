# # Increament an attribute value through a method
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
#     def increment_odometer(self,miles):
#         """Add the miles to the odometer reading of the car"""
#         self.odometer_reading += miles

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.update_odometer(33)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(400)
# my_new_car.read_odometer()

# # Inheritance
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
#     def increment_odometer(self,miles):
#         """Add the miles to the odometer reading of the car"""
#         self.odometer_reading += miles



# class ElectricCar(Car):
#     def __init__(self, make, model, year, battery = "10kw"):
#         super().__init__(make,model,year)
#         self.battery = battery
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model + ' battery power' +self.battery
#         return long_name.title()

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.update_odometer(33)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(400)
# my_new_car.read_odometer()

# my_electric_car = ElectricCar("tata", "nexon", 2020)
# my_electric_car.update_odometer(45)
# print(my_electric_car.get_descriptive_name())
# my_electric_car.read_odometer()

# # Instance as attribute
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
#     def increment_odometer(self,miles):
#         """Add the miles to the odometer reading of the car"""
#         self.odometer_reading += miles

# class Battery:
#     """ """
#     def __init__(self, battery_size = 70):
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """ """
#         print("The battery size is "+ str(self.battery_size))

# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make,model,year)
#         self.battery = Battery()

#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model + ' battery power' + str(self.battery.battery_size)
#         return long_name.title()

# # my_new_car = Car('audi', 'a4', 2016)
# # print(my_new_car.get_descriptive_name())
# # my_new_car.read_odometer()
# # my_new_car.update_odometer(33)
# # my_new_car.read_odometer()
# # my_new_car.increment_odometer(400)
# # my_new_car.read_odometer()

# my_electric_car = ElectricCar("tata", "nexon", 2020)
# my_electric_car.update_odometer(45)
# print(my_electric_car.get_descriptive_name())
# my_electric_car.read_odometer()
# my_electric_car.battery.describe_battery()


# Import class
from battery import Battery
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
    def increment_odometer(self,miles):
        """Add the miles to the odometer reading of the car"""
        self.odometer_reading += miles

# class Battery:
#     """ """
#     def __init__(self, battery_size = 70):
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """ """
#         print("The battery size is "+ str(self.battery_size))

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model + ' battery power' + str(self.battery.battery_size)
        return long_name.title()

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.update_odometer(33)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(400)
# my_new_car.read_odometer()

#print("Battrey class is imported")
# my_electric_car = ElectricCar("tata", "nexon", 2020)
# my_electric_car.update_odometer(45)
# print(my_electric_car.get_descriptive_name())
# my_electric_car.read_odometer()
# my_electric_car.battery.describe_battery()