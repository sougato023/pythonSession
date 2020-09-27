#List: A collection of items in a particular order

motorcycles = ["hero", "suzuki","honda", "suzuki"]
print(motorcycles)
# access a spectic list element
print(motorcycles[0].upper())

message = "My first motorcycle was '"+ motorcycles[0].title() + "'."
print(message)

#adding elemnt to list: append
motorcycles.append("ducati")
print(motorcycles)

bicycles = []
bicycles.append("hero")
bicycles.append("cannondale")

#adding element using insert
motorcycles.insert(0,"bmw")
print(motorcycles)

#remove an element
# removed_element = motorcycles[0]
# del motorcycles[0]
# print("I have sold my "+ removed_element)


#removed_element = motorcycles.pop()
#print("I have sold my "+ motorcycles.pop(1)) # with index in pop method it will remove the specific element. without index it will remove the last element in the list
#print(motorcycles)
#remove using remove
motorcycles.remove("suzuki")
print(motorcycles)

#sorting a list:permanent
# motorcycles.sort(reverse = True)
# print(motorcycles)

# temporary sorting
sorted_list = sorted(motorcycles)
print("Sorted list : "+ str(sorted_list))
print("Original List : "+str(motorcycles))
# permanent reverse
motorcycles.reverse()
print("List in reverse order : "+str(motorcycles))

print(len(motorcycles))

age = 23
print("My age is : "+str(age))