# Black Jack game.
import blackjack

should_continue = True

user_name = input("What is your name? ")

player = blackjack.create_player(name=user_name, hand=blackjack.draw(2), type="player")

machine = blackjack.create_player(name="Pc", hand=blackjack.draw(2), type="computer")

while should_continue:

    user_score = blackjack.sum_cards_on_hand(player["player_hand"])
    computer_score = blackjack.sum_cards_on_hand(machine["player_hand"])

    print(f"Hey {player["player_name"]} your hand is {player["player_hand"]}!")
    print(f"The dealer's hand is {machine["player_hand"][0]}")

    user_has_blackjack = blackjack.check_for_blackjack(player["player_hand"])
    computer_has_blackjack = blackjack.check_for_blackjack(machine["player_hand"])

    if user_has_blackjack:
        should_continue = False
        print(f"The player: {player["player_name"]} won the game 'cause he's got an BLACKJACK!! The player {machine["player_name"]} LOST!!")
        continue
    elif computer_has_blackjack:
        should_continue = False
        print(f"The player: {machine["player_name"]} won the game 'cause he's got an BLACKJACK!! The player {player["player_name"]} LOST!!")
        continue

    if blackjack.over_21(player["player_hand"]):
        print(f"The {player["player_name"]} has more than 21, he looses!")
        should_continue = False
        continue

    extra_card = input("Do you want to get an extra card? [Y / N] ").lower()

    if extra_card == 'y':
        player["player_hand"] = blackjack.draw_extra(player["player_hand"])
        print(player["player_hand"])
        continue

    while blackjack.under_17(machine["player_hand"]):
        print("Adding a card to Dealer's hand.")
        machine["player_hand"] = blackjack.draw_extra(machine["player_hand"])
        if blackjack.over_21(machine["player_hand"]):
            print(f"The Dealer has gone over 21!")
            print(f"Dealer's hand is {machine["player_hand"]}")
            should_continue = False
            continue
    
    if blackjack.over_21(machine["player_hand"]):
        print(f"The {machine["player_name"]} has more than 21, he looses! {player["player_name"]} WON!!")
        should_continue = False
        continue
    
    game_result = blackjack.compare_hands(player_hand=player["player_hand"], dealer_hand=machine["player_hand"])

    if game_result == 'Player won.':
        should_continue = False
        print(f"Player hand: {player["player_hand"]}")
        print(f"Dealer hand: {machine["player_hand"]}")
        print(f"The player {player["player_name"]} WON!!!!")
        continue
    elif game_result == "Dealer won.":
        should_continue = False
        print(f"Player hand: {player["player_hand"]}")
        print(f"Dealer hand: {machine["player_hand"]}")
        print(f"The player {machine["player_name"]} WON!!!!")
        continue
    elif game_result == "It's a tie.":
        should_continue = False
        print(f"Player hand: {player["player_hand"]}")
        print(f"Dealer hand: {machine["player_hand"]}")
        print("Both got the same pontuation, it's a TIE!!!")
        continue
