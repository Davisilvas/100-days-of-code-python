"""
    This class is about Dictionary in Python
    The dict is a set of Key and Value
"""
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Loop"]) # -> Will print only the value, not the key.

# Adding nem items
programming_dictionary["Test"] = "This is a test."

print(programming_dictionary)

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)
# - > This may be useful to wipe user data, like in game for example

# How to loop through a dictionary
print("#" * 15)
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
