# def get_highest_bid(dict):
#     x = 0
#     player = ''
#     auct_winner = {}
#     for enter in dict:
#         if dict[enter] > 0:
#             x = dict[enter]
#             player = enter
#     auct_winner[player] = x
#     return auct_winner

#from replit import clear
import art

print(art.logo)
print("Welcome to the secret auction program.")

restart = True
bids = {}

def add_bid_to_dict(name, bid):
    bids[name] = bid

def get_highest_bid(dict_input):
    x = 0
    player = ''
    for enter in dict_input:
        if dict_input[enter] > x:
            x = dict_input[enter]
            player = enter
    return f"The Winner of this silent auction is: {player} with an auction of ${x}."

while restart:
    name_input = input("What's your name?\n").lower()
    bid_input = int(input("What's your bid?\n$"))

    add_bid_to_dict(name=name_input, bid=bid_input)

    restart_answer = input("Do you want to bid? Type 'yes' or 'no'.\n").lower()
    if restart_answer ==  'no':
        restart = False

winner = get_highest_bid(bids)
print(winner)
