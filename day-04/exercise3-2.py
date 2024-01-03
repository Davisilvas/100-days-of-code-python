line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
treasure_map = [line1, line2, line3]

position = input("Hidding your treasure! X marks the spot!\n").capitalize()
letter = position[0].lower()
abc = ['a', 'b', 'c']
letter_index = abc.index(letter)
number_index = int(position[1]) - 1

treasure_map[number_index][letter_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")
