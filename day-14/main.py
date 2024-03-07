from game_functions import get_random_item, get_followers, show_data, compare_followers
import art

print(art.logo)

hits = 0
should_continue = True

item_a = get_random_item()
item_b = get_random_item()

while should_continue:
    if item_a == item_b:
        item_b == get_random_item()
        continue
    
    print(f"Compare A: {show_data(item_a)}")
    print(art.vs)
    print(f"Against B: {show_data(item_b)}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_choice == 'a':
        selected = item_a
        other = item_b
    else:
        selected = item_b
        other = item_a
    
    if get_followers(selected) > get_followers(other):
        hits += 1
        item_a = selected
        item_b = get_random_item()
        continue
    else:
        print(f"You guessed wrong :/ You made {hits} points.")
        should_continue = False
