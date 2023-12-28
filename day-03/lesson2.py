# -> Nested if statements

print("Welcome to Frontin's Roller Coaster!")

height = int(input("Please enter your height: "))
age = int(input("Please enter your age: "))

if height >= 120:
    print("You are allowed to go")

    if age >= 18:
        print("The price is $12 dolars")
    elif age > 12 and age < 17:
        print("The price is $7 dolars")
    else:
        print("The price is $5 dolars")
else:
    print("We're sorry, only people with at least 1.20 meters are allowed :(")
