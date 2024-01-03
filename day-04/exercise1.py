import random

print("Welcome to the virtual coin toss!")

user_guess = input("What is your guess? heads or tails?").lower().capitalize()

random_result = random.randint(0, 1)

coin = ''

if random_result == 1:
    coin = 'Heads'
else: 
    coin = 'Tails'

if user_guess == coin:
    print(f"Dude you won! The coin flipped to {user_guess} as you predicted!")
else:
    print(f"We're sorry man, u lost. The coin is {coin} and you guessed {user_guess}")
