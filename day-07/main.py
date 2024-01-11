import random
import arts
import hangman_words
word_list = hangman_words.word_list

#chosen_word = word_list[random.randint(0, len(word_list) - 1)]
chosen_word = random.choice(word_list)
print(arts.logo)
print(f"pssst,the solution is {chosen_word}.")

display = []
for letter in chosen_word:
    display.append("_")

end_of_game = False
lives = 6
guesses = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print("Sir you already entered that letter, try another one.\nHere are the letters you've already tryed")
        print(f"{' '.join(guesses)}")
        print("And here is how the game is going so far:")
        print(f"{' '.join(display)}")
    else:
        if guess in chosen_word:
            for index in range(len(chosen_word)):
                letter = chosen_word[index]
                if letter == guess:
                    display[index] = guess
            

        if guess not in chosen_word:
            lives -= 1
            print(f"The letter \"{guess}\" isn't in the word!")
            if lives == 0:
                print("you suck, looser!")
                end_of_game = True
        print(f"{' '.join(display)}")
        print(arts.stages[lives])

    if '_' not in display:
        end_of_game = True
        print("You Won!!")
    guesses.append(guess)
