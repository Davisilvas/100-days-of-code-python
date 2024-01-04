even_numbers_sum = 0

wished_input = int(input("input an even number. "))

if (wished_input <= 1000) and (wished_input % 2 == 0):
    for n in range(2, wished_input + 1, 2):
        even_numbers_sum += n

    print(even_numbers_sum)
else:
    print("Please run the code again and input a number that is bellow 1000 and even")
