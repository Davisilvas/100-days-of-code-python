print(8 * "*")
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print(8 * "*")

direction = input(
    "Wich direction you wanna go? \"Left\" or \"Right?\" ").lower()

if direction.lower() == 'left':
    river_stage = input(
        "There is a river, you want to wait for a boat or swim? ")

    if river_stage.lower() == "wait":
        print("There are three doors. A yellow, a blue and a red one")
        door_stage = input("Wich one do you choose? ")

        if door_stage.lower() == "yellow":
            print("You Won!!!! U found the treasure!!!")
        elif door_stage.lower() == "blue":
            print("A knight killed u in a sword combat.")
        else:
            print("A dragon was behind the door and burned you down.")
    else:
        print("An enormous crocodile ate u, game over :/")
else:
    print("U felt into a hole, game over :/")
