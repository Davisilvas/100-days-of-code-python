"""
How to modify Variables 
with global scope
"""

enemies = 1

def increase_enemies():
    global enemies
    enemies += 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
increase_enemies()
increase_enemies()
print(f"enemies inside function: {enemies}")
