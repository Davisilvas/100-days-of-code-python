line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
treasure_map = [line1, line2, line3]

position = input("Hidding your treasure! X marks the spot!\n").capitalize()

if position == 'A1':
    line1[0] = 'X'
elif position == 'A2':
    line2[0] = 'X'
elif position == 'A3':
    line3[0] = 'X'
elif position == 'B1':
    line1[1] = 'X'
elif position == 'B2':
    line2[1] = 'X'
elif position == 'B3':
    line3[1] = 'X'
elif position == 'C1':
    line1[2] = 'X'
elif position == 'C2':
    line2[2] = 'X'
elif position == 'C3':
    line3[2] = 'X'
else:
    print("ENTER A VALID OPTION!")

print(f"{line1}\n{line2}\n{line3}")
