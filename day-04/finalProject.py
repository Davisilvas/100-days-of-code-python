import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

rps = ["Rock", "Paper", "Scissors"]

if (user_choice >= 0) and (user_choice <=2):
    if rps[user_choice] == 'Rock':
        if rps[computer_choice] == 'Scissors':
            print(f"You choose {rps[user_choice]} and the PC choose {rps[computer_choice]}. You WIN")
        if rps[computer_choice] == 'Paper':
            print(f"You choose {rps[user_choice]} and the PC choose {rps[computer_choice]}. You LOST")

    if rps[user_choice] == 'Paper':
        if rps[computer_choice] == 'Scissors':
            print(f"You choose {rps[user_choice]} and the PC choose {rps[computer_choice]}. You LOST")
        if rps[computer_choice] == 'Rock':
            print(f"You choose {rps[user_choice]} and the PC choose {rps[computer_choice]}. You WIN")

    if rps[user_choice] == 'Scissors':
        if rps[computer_choice] == 'Paper':
            print(f"You choose {rps[user_choice]} and the PC choose {rps[computer_choice]}. You WIN")
        if rps[computer_choice] == 'Rock':
            print(f"You choose {rps[user_choice]} and the PC choose {rps[computer_choice]}. You LOST")

    if rps[user_choice] == rps [computer_choice]:
        print("it's a draw guys")
else:
    print("You typed an invalid option mate.")
