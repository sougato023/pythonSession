#functions
# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")
# greet_user()

# #passing information to a function
# def greet_user(username):
#     """Display a simple greeting."""
#     print("Hello, " + username.title() + "!")
# greet_user('sonu')

#positional arguments
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('rabbit', 'rocky')
# describe_pet("dog","sammy")
# #multiple functio call
#describe_pet('dog', 'willie')

#order maters in positiona arguments

#keyword arguments
# describe_pet(animal_type='rabbit', pet_name='rocky')
# describe_pet(pet_name='rocky', animal_type='rabbit')

# #default values
# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet(pet_name='willie')
#describe_pet("willie")

# describe_pet(pet_name='rocky', animal_type='rabbit')

#equivalent function calls
# A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')
# # # A hamster named Harry.
# describe_pet('rocky', 'rabbit')
# describe_pet(pet_name='rocky', animal_type='rabbit')
# describe_pet(animal_type='rabbit', pet_name='rocky')

#return values

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('sougato', 'chakraborty')
# print(musician)

#optional arguments
# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('nikhil', 'kumar', 'chakraborty')
# musician = get_formatted_name('sougato', 'chakraborty')
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('sougato', 'chakraborty')
# print(musician)
# musician = get_formatted_name('nikhil', 'chakraborty', 'kumar')
# print(musician)

#return a dictionary
# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name,'age':22}
#     return person

# musician = build_person('sougato', 'chakraborty')
# print(musician)
# print("Age: "+str(musician["age"]))


#passing a list
# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)

# usernames = ['sam', 'sonu', 'tina']
# greet_users(usernames)

# #modifying a list
# # Start with some designs that need to be printed.
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     # Simulate creating a 3D print from the design.
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)

 
# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


# def print_models(param_unprinted_designs, param_completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
#     while param_unprinted_designs:
#         current_design = param_unprinted_designs.pop()
#         # Simulate creating a 3D print from the design.
#         print("Printing model: " + current_design)
#         param_completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


#arbitrary arguements
# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')