print("Leap year checker!")

year_to_check = int(input("Please, enter the year you want to check:\n"))

if(year_to_check % 4 == 0 or year_to_check % 400 == 0):
    print(f"{year_to_check} is a leap year!")
else:
    print(f"{year_to_check} isn't a leap year!")
