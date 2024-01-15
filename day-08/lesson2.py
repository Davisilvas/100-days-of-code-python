#multiple inputs

def grade_maker(g1, g2):
    grade = (g1 + g2) / 2
    return grade

# -> This one was called with positional arguments
print(grade_maker(7, 8))

# -> This one was called with keywords arguments
print(grade_maker(g2 = 2, g1 = 10))
