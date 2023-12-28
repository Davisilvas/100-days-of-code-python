print("Bem vindo à calculadora de IMC")

weight = input("Please, inform your weight:\n")
height = input("Please, inform your height:\n")

BMI = float(weight) / float(height) ** 2

print(f"Your BMI is: {BMI:.0f}")
