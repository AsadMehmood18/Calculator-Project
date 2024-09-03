from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
result = 0
while True:
    if result != 0:
        print("+")
        print("-")
        print("*")
        print("/")
        symbol = input("Pick an operation: ")
        number_2 = float(input("What's the next number?: "))
        next_result = operations[symbol](result, number_2)
        print(f"{result} {symbol} {number_2}= {next_result}")
        end = input(f"Type 'y' to continue calculating with {next_result}, or type 'n' to start a new calculation: ").lower()
    else:
        number_1 = float(input("What's the first number?: "))
        print("+")
        print("-")
        print("*")
        print("/")
        symbol = input("Pick an operation: ")
        number_2 = float(input("What's the next number?: "))
        result = operations[symbol](number_1, number_2)
        print(f"{number_1} {symbol} {number_2}= {result}")
        end = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if end == 'n':
        result = 0
        continue
    elif end == 'y':
        continue
    else:
        break
