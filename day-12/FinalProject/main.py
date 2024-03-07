import random
random_number = random.randint(1, 100)

print("Welcom to guessing game.")
print("I'm thinking a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def checking_the_guess(correct_number, guess):
    is_right = False

    if guess == correct_number:
        print(f"You won! {guess} is the number I was thinking!")
        is_right = True
    elif guess > correct_number:
        print(f"Too high. {guess} wasn't the number I was thinking.")
    elif guess < correct_number:
        print(f"Too low. {guess} wasn't the number I was thinking.")
    return is_right

attempts = 0
if difficulty == 'easy':
    attempts = 10
    print("You have 10 attempts to win the game")
elif difficulty == 'hard':
    attempts = 5
    print("You have 05 attempts to win the game")

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    current_try = checking_the_guess(random_number, user_guess)
    if current_try:
        break
    attempts -= 1 