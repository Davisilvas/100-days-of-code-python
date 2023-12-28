print("Is it odd or even?!")

number = int(input("Please enter a number to discover if it's odd or even!\n"))

calc = number % 2 # -> this could go directly in the if statement

if calc == 0:
    print(f"The number {number} is even!")
else:
    print(f"The number {number} is odd!")

# MODULO SIGN IS %
