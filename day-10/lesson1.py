def format_name(name, last_name):
    name_capitalized = name.title
    () + ' ' + last_name.title()
    return name_capitalized

name_input = input("Name: ")
last_name_input = input("Last name: ")

print(format_name(name=name_input, last_name=last_name_input))
