student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermioni": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

def grade_avaliator(grade):
    if (grade <= 100) and (grade >= 91):
        return "Outstanding"
    elif (grade <= 90) and (grade >= 81):
        return "Exceeds expectations"
    elif (grade <= 81) and (grade >= 70):
        return "Acceptable"
    else:
        return "Fail"

for student in student_scores:
    student_grades[student] = grade_avaliator(grade=student_scores[student])
