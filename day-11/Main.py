# Black Jack game.
import blackjack

should_continue = True

user_name = input("WHat is your name? ")

player = blackjack.create_player(name=user_name, hand=blackjack.draw(2), type="player")

machine = blackjack.create_player(name="Pc", hand=blackjack.draw(2), type="computer")

print(f"Welcome {player["player_name"]}, let's have a game! Your hand is {player["player_hand"]}")

while should_continue:






    should_continue = False























# test_hand = draw(2)
# test_total = sum_cards_on_hand(test_hand)
# test_check_for_blackjack = check_for_blackjack(test_hand)

# test_hand_2 = [10, 11, 2, 9]
# print(f"teste over 21 --- {over_21(test_hand_2)}")

# print(test_hand)
# print(test_total)
# print(test_check_for_blackjack)
# print(blackjack_message(test_check_for_blackjack, "Player 1"))
