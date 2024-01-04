print("Hi Welcome to the student average height calculator.")

students_heights = input("Insert all the data without \".\" please.\n").split(", ")

total_in_centimeters = 0
number_of_students = 0

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
    total_in_centimeters += students_heights[n]
    number_of_students += 1

average_height = total_in_centimeters // number_of_students
print(15 * "- |" + ' -')
print(f"Total height: {total_in_centimeters}")
print(f"Number of students: {number_of_students}")
print(f"Average height: {average_height}")
