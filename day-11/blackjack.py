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

def draw_extra(hand):
    new_hand = []
    for x in hand:
        new_hand.append(x)
    new_hand.append(random.choice(cards))
    return new_hand

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

def check_for_ace(hand):
    has_ace = False
    if 11 in hand:
        has_ace = True
    return has_ace

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
        if check_for_ace(hand):
            total -= 10
            if total <= 21:
                is_over_21 = False
    return is_over_21

def under_17(hand):
    is_under_17 = False
    total = sum_cards_on_hand(hand)
    if total < 17:
        is_under_17 = True
    return is_under_17

def compare_hands(player_hand, dealer_hand):
    player_total = sum_cards_on_hand(player_hand)
    dealer_total = sum_cards_on_hand(dealer_hand)

    result = ''

    if (not over_21(player_hand)) and (not over_21(dealer_hand)):
        if player_total > dealer_total:
            result = "Player won."
        elif dealer_total > player_total:
            result = "Dealer won."
        elif player_total == dealer_total:
            result = "It's a tie."
    
    return result