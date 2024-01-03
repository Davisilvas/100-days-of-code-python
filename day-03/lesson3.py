# Multiple if statements in succession
print("Welcome to Frontin's Roller Coaster!")

height = int(input("Please enter your height: "))
age = int(input("Please enter your age: "))
total_to_pay = 0

if height >= 120:
    print("You are allowed to go")

    if age >= 18:
        print("The adult ride is $12 dolars")
        total_to_pay = 12
    elif age > 12 and age < 17:
        print("The youth ride is $7 dolars")
        total_to_pay = 7
    else:
        print("The child ride is $5 dolars")
        total_to_pay = 5

    want_the_photo = input("Do you want the photo of the ride? (Y / N)\n")

    if want_the_photo == 'Y':
        total_to_pay += 3

    print(f"Your bill is ${total_to_pay}.")
else:
    print("We're sorry, only people with at least 1.20 meters are allowed :(")
