print("Welcome to Python Pizza! What is your order?")

size = input("What size pizza do you want? (S, M, L)\n")
add_pepperoni = input("Do you want pepperoni? (Y or N)\n")
extra_cheese = input("Do you want extra cheese? (Y or N)\n")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("please input a valid option for the size!")

if add_pepperoni == "Y" and size == "S":
    bill += 2

if add_pepperoni == "Y" and (size == "M" or size == "L"):
    bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is ${bill}.")
