from art import logo
print(logo)

# adding various functionalities

def add(n1 , n2):
    return n1+n2

def subtract(n1 , n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply
}

def calculate(number1 , number2):
    operation_symbol = input("Pick another symbol: ")
    calculation_function = operations[operation_symbol]
    answer_function = calculation_function(number1,number2)
    return f"The result is {number1} {operation_symbol} {number2} = {answer_function}"

calc_status = True
while calc_status:

    num1 = int(input('What is your first number? '))

    for item in operations:
        print(item)
    operation_symbol = input("Pick an operation symbol from the one's given above: ")

    num2 = int(input('What is your second number? '))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    print(f"The result is {num1} {operation_symbol} {num2} = {answer}")

    calc_active = True
    while calc_active:
        calc_continue = input("Type y if you want to continue calculation or n if you dont want to continue: ")
        if calc_continue == "n":
            calc_active = False
            calc_status = False
        elif calc_continue == "y":
            print(calculate(answer , int(input("Enter next number: "))))
