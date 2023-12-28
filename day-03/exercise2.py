print("Welcome to BMI calculator!")

user_height = float(input("Please enter your height:\n"))
user_weight = float(input("Please enter your weight:\n"))

user_BMI = user_weight / user_height ** 2

if user_BMI >= 35.0:
    print(f"Your BMI is {user_BMI:.2f} and you are clinically obese.")
elif user_BMI >= 30.0:
    print(f"Your BMI is {user_BMI:.2f} and you are obese.")
elif user_BMI >= 25.0:
    print(f"Your BMI is {user_BMI:.2f} and you are slightly overweight.")
elif user_BMI >= 18.5: 
    print(f"Your BMI is {user_BMI:.2f} and you have a normal weight.")
else:
    print(f"Your BMI is {user_BMI:.2f} and you are under weight.")