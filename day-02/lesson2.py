# len function does not accept integers, but returns it.
# the function type() checks the type of the data inputed in it.

num_char = len(input("What is your name? "))

print(type(num_char))  # -> should return <class 'int'>

# *** TYPE CASTING ***
# -> The function str() casts the informed data into a string.

casted_num_char = str(num_char)
print(type(casted_num_char))

# -> The function float() casts an integer, or numeric string into a float
x = "100.7"
print(float(x))
print(type(float(x)))
