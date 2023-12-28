# F strings in Python

x = 8 / 3
print(x)

# The function round() with just one argument will round the number to an integer
# But if it does recive an argument, the second one will be the number of cases after the . (dot)
# But it will round up if it can be done.
# not so good if precise numbers are necessary

x = round(x, 2)
print(x)

# FLOOR DIVISION
# With 2 // we make the floor division, wich will cut all the floating numbers.
# and returns an int

y = 8 // 3
print(y)

# --------------
# += | -= | *=
score = 0
score += 1
score += 1
score += 1

print(score)

# F STRINGS
print(f"your score is {score} and x value is {x}")
