# # Reading an entire file
# with open("pi_digits.txt") as file_object:
#     contents = file_object.read()
#     print(contents)
 

# # Reading files by line
# # filename = ".\..\data\pi_digits.txt"
# filename = ".\..\..\..\sampleData\data.txt"
# # filename = ".\..\..\..\sampleData\users\data.txt"
# with open(filename) as file_object:
#     for line in file_object:
#         print(line)


# #Making a list of line from a file
# filename = '..\..\data\pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.strip())

# #working with file contents
# filename = '..\..\data\pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()

# print(pi_string)
# print(len(pi_string))

# #large files
# filename = 'pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string[:52] + "...")
# print(len(pi_string))


# filename = 'pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()

# birthday = input("Enter your birthday, in the form mmddyy: ")

# if birthday in pi_string:
#         print("Your birthday appears in the first million digits of pi!")
# else:
#         print("Your birthday does not appear in the first million digits of pi.")


# #writing to file
# #write a empty file
# filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.")


# #write multiple lines
# filename = 'programming.txt'
# with open(filename, 'w') as file_object:
#     file_object.write("I love python programming an nodejs programming.")
#     file_object.write("I love creating new games.")

#appending to a file
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("\n\tI also love finding meaning in large datasets.\n")
    file_object.write("\tI love creating apps that can run in a browser.\n")


