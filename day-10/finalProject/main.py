import art

def add(n1, n2):
    return n1 + n2

def subtraction (n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def printing_operations(op_dict):
    for op in op_dict:
        print(op)

opertations = {
    "+": add,
    "-": subtraction,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)

    num1 = float(input("What's the first number? "))
    printing_operations(opertations)
    should_continue = True

    while should_continue:
        opertations_input = input("Which operation you wanna use? ")
        num2 = float(input("What's the second number? "))
        calculation_function = opertations[opertations_input]
        answer = calculation_function(n1=num1, n2=num2)
        print(f"{num1} {opertations_input} {num2} = {answer}")

        retry = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation.: ").lower()
        if retry == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
