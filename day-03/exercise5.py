name1 = input("What is your name? ")
name2 = input("What is their name? ")

T_occurances = 0
R_occurances = 0
U_occurances = 0
E_occurances_true = 0
TRUE_total = 0

L_occurances = 0
O_occurances = 0
V_occurances = 0
E_occurances_love = 0
LOVE_total = 0

T_occurances += name1.count("T")
R_occurances += name1.count("R")
U_occurances += name1.count("U")
E_occurances_true += name1.count("E")

T_occurances += name2.count("T")
R_occurances += name2.count("R")
U_occurances += name2.count("U")
E_occurances_true += name2.count("E")

L_occurances += name1.count("L")
O_occurances += name1.count("O")
V_occurances += name1.count("V")
E_occurances_love += name1.count("E")

L_occurances += name2.count("L")
O_occurances += name2.count("O")
V_occurances += name2.count("V")
E_occurances_love += name2.count("E")

TRUE_total = T_occurances + R_occurances + U_occurances + E_occurances_true
LOVE_total = L_occurances + O_occurances + V_occurances + E_occurances_love

TRUE_total = str(TRUE_total)
LOVE_total = str(LOVE_total)

points = int(TRUE_total + LOVE_total)

# print(type(TRUE_total))
# print(type(LOVE_total))
# print(points)

if points > 0:
    if points <= 10 or points >= 90:
        print(f"Your score is: {points}, you go like coke and mentos")
    if points >= 40 and points <= 50:
        print(f"Your score is {points}, you're alright together")
    print(f"your score is {points}.")
