import random
import stages
word_list = ["advark", "baboon", "camel"]

#chosen_word = word_list[random.randint(0, len(word_list) - 1)]
chosen_word = random.choice(word_list)
print(f"pssst,the solution is {chosen_word}.")

display = []
for letter in chosen_word:
    display.append("_")

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for index in range(len(chosen_word)):
            letter = chosen_word[index]
            if letter == guess:
                display[index] = guess
        
        print(str(display))

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("you suck, looser!")
            end_of_game = True
    print(stages.stages[lives])

    if '_' not in display:
        end_of_game = True
        print("You Won!!")
