#Looping through a list
motorcycles = ["hero", "suzuki","honda", "suzuki"]
for motorcycle in motorcycles:
    print("I have \"" + motorcycle.upper() + "\" in my garage")
    print("I want to buy another bike for myself")
    
print("Thank you for viewing by garage")

#numerical list using range

# for value in range(1,5):
#     print(value)


# for(int i= 0; i <motorcycles.length;i++){
# motorcycle = motorcycles[i]
# }

#using range to make a list of numbers

# number_list = list(range(1,10,3))
# print(number_list)
# for number in number_list:
#     print(number**2)

#simple statistics with numbers
# digit = [1,3,10,9,8,21,0,13]
# print(min(digit))
# print(max(digit))
# print(sum(digit))

#List comprehensions
# squares = [value ** 3 for value in range(1,20,2)]
# print(squares)

#Slicing a list
# motorcycles = ["hero", "suzuki","honda", "ducati",1,2,34,57,98,True]
# print(motorcycles)

# motorcycles_brand = motorcycles[:9]
# print(motorcycles_brand)
#copying a list
motorcycles = ["hero", "suzuki","honda", "ducati",1,2,34,57,98,True]
motorcycles_copy_list = motorcycles[:]
print(motorcycles_copy_list)
motorcycles[0] = "bmw"
print(motorcycles)