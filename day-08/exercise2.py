def prime_checker(number):
    is_prime = False
    if (number % 1 == 0) and (number % number == 0):
        is_prime = True
    for x in range(2, 101):
        if x == number:
            continue
        if number % x == 0:
            is_prime = False
    if number == 1:
        is_prime: False
    if is_prime:
        print(f"The number {number} is a prime number!")
    else:
        print(f"The number {number} ISN'T a prime number")
    #return is_prime



n = int(input("Number to check if it's a prime number: "))
#prime_checker(number = n)
index = 1
while index < 101:
    prime_checker(number=index)
    index += 1
