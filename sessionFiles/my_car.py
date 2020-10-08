# from Example15_2 import Car
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.update_odometer(33)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(400)
# my_new_car.read_odometer()

# #import multiple classes

# from Example15_2 import Car,ElectricCar
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.update_odometer(33)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(400)
# my_new_car.read_odometer()

# print("Battrey class is imported")
# my_electric_car = ElectricCar("tata", "nexon", 2020)
# my_electric_car.update_odometer(45)
# print(my_electric_car.get_descriptive_name())
# my_electric_car.read_odometer()
# my_electric_car.battery.describe_battery()

#import multiple classes

import Example15_2
my_new_car = Example15_2.Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(33)
my_new_car.read_odometer()
my_new_car.increment_odometer(400)
my_new_car.read_odometer()

print("Battrey class is imported")
my_electric_car = Example15_2.ElectricCar("tata", "nexon", 2020)
my_electric_car.update_odometer(45)
print(my_electric_car.get_descriptive_name())
my_electric_car.read_odometer()
my_electric_car.battery.describe_battery()