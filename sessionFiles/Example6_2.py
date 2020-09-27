# a simple example
# cars = ['audi', 'bMW', 'suzuki', 'toyota']
# for car in cars:
#     if car.lower() == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

#ignoring cases

#numerical comparison
# age = 19
# if age >= 18:
#     print("You are old enough to vote!")

# age = 17
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")




# age = 12

# if age < 4:
#     print("Your admission cost is $0.")

# elif age < 18:
#     print("Your admission cost is $5.")
# else:
#     print("Your admission cost is $10.")


# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# elif age >= 65:
#     price = 5
# print("Your admission cost is $" + str(price) + ".")

# #check for inequality


#check multiple conditions
# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
# print("\nFinished making your pizza!")


# requested_toppings = ['mushrooms', 'extra cheese']
# for topings in requested_toppings:
#     if 'mushrooms' in topings:
#         print("Adding mushrooms.")
#     elif 'pepperoni' in topings:
#         print("Adding pepperoni.")
#     elif 'extra cheese' in topings:
#         print("Adding extra cheese.")
# print("\nFinished making your pizza!")

#using if-else in list
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print("Adding " + requested_topping + ".")
# print("\nFinished making your pizza!")


available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")


print("\nFinished making your pizza!")