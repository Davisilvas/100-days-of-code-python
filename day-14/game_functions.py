import game_data
import random

def get_random_item ():
    selected_item = random.choice(game_data.data)
    return selected_item

def show_data(item):
    return f"{item["name"]}, {item["description"]}, from {item["country"]}."

def get_followers(item):
    return item["follower_count"]

def compare_followers(item_a, item_b):
    counter = 0
    if get_followers(item_a) > get_followers(item_b):
        counter = get_followers(item_a)
    else:
        counter = get_followers(item_b)
    return counter