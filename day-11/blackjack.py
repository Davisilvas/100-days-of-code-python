import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def create_player(name, hand, type):
    if type == "player" or type == "computer" or type == "pc":
        new_player = {
            "player_name": name,
            "player_hand": hand,
            "player_type": type
        }
        return new_player
    return "please enter a valid value for 'type'."

def draw(number_of_cards):
    x = 0
    hand = []
    while x < number_of_cards:
        hand.append(cards[random.randrange(0, len(cards))])
        x += 1
    return hand

def sum_cards_on_hand(hand):
    total = 0
    for x in hand:
        total += x
    return total

def check_for_blackjack(hand):
    has_blackjack = False
    if (11 in hand) and (10 in hand):
        has_blackjack = True
    return has_blackjack

def blackjack_message(hand, player):
    message = f"{player} does not have a blackjack"
    if hand:
        message = f"{player} won the game for having a blackjack"
    return message

def over_21(hand):
    is_over_21 = False
    total = sum_cards_on_hand(hand)
    if total > 21:
        is_over_21 = True
        if check_for_blackjack(hand):
            total -= 10
            if total > 21:
                is_over_21 = True
            else:
                is_over_21 = False
    return is_over_21

def under_17(hand, player):
    new_hand = hand
    if player == "computer" or player == "pc":
        total = sum_cards_on_hand(hand)
        if total < 17:
            new_hand.append(draw(1))
    return new_hand
