import math

test_h = float(input("Input the height of the wall: "))
test_w = float(input("Input the width of the wall: "))

coverage = 5

def paint_calc(height, width):
    number_of_cans = (height * width) / coverage
    round_up_cans = math.ceil(number_of_cans)
    return f"You'll need {round_up_cans} cans of paint."

x = paint_calc(height= test_h, width= test_w)
print(x)
