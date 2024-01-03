import random

print("Welcome to the Banker Roulette")

names_string = input("Insert the names here!\n")

names = names_string.split(", ")

random_index = random.randint(0, len(names) -1)

print(f"Well, the unlucky of the night is {names[random_index]} that is going to pay for everyone!")
