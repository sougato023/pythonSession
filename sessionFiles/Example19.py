#Exceptions
# If you write code
# that handles the exception, the program will continue running. If you don’t
# handle the exception, the program will halt and show a traceback, which
# includes a report of the exception that was raised.
# Exceptions are handled with try-except blocks. A try-except block asks
# Python to do something, but it also tells Python what to do if an exception
# is raised. When you use try-except blocks, your programs will continue
# running even if things start to go wrong. Instead of tracebacks, which can
# be confusing for users to read, users will see friendly error messages that
# you write.

#Handlling zero division error exception
# print(5/0)
# print("Hello Python prorammer!!!")

# # # #using try-except blocks
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# print("Hello Python prorammer!!!")

# #using exceptions to avoid crashes
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)




# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:    
#         print(answer)


# #Handling file not found exception
# filename = 'alice.txt'
# with open(filename) as f_obj:
#     contents = f_obj.read()


# filename = 'alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()

# except FileNotFoundError:
#     msg = "Sorry, the file " + filename + " does not exist."
#     print(msg)


#Analyzing text
# >>> title = "Alice in Wonderland"
# >>> title.split()
# ['Alice', 'in', 'Wonderland']


# filename = 'alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = "Sorry, the file " + filename + " does not exist."
#     print(msg)

# else:
# # Count the approximate number of words in the file.
#     words = contents.split()
#     print("Text words: "+str(words))
#     num_words = len(words)
#     print("The file " + filename + " has about " + str(num_words) + " words.")


# #Storing data
# import json

# numbers = [2, 3, 5, 7, 11, 13]
# filename = 'numbers.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)

# import json

# filename = 'numbers.json'
# with open(filename) as f_obj:
#     numbers = json.load(f_obj)
# print(numbers)

# # #storing and reading user-generated data
# import json

# username = input("What is your name? ")
# filename = 'username.json'
# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print("We'll remember you when you come back, " + username + "!")


# import json
# filename = 'username.json'
# with open(filename) as f_obj:
#     username = json.load(f_obj)
#     print("Welcome back, " + username + "!")

# #combine the above two programs
import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")