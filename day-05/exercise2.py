student_scores = input("Input the scores here \n").split()

max_score = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if student_scores[n] > max_score:
        max_score = student_scores[n]

print(f"The highest score in the class is: {max_score}")
