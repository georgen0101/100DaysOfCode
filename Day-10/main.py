"""
100 Days Of Code - George
Python Calculator
"""
from art import logo
from replit import clear
# Operator functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Create a dictionay where the key is the symbol e.g. "+" and the values are the name of the functions e.g. "add"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    # Ask for num1
    num1 = float(input("What's the first number?: "))
    
    # Use a for loop to print the symbols
    for symbol in operations:
        print(symbol)
    # ANSWER
    last_answer = num1
    
    is_active = True
    while is_active:
        # Ask the user for which operation wants to use
        operation_symbol = input("Pick an operator: ")
        
        # Ask for num2 
        num2 = float(input("What's the next number?: "))
        
        # Make the operation that the user want with the numbers
        calculation_function = operations[operation_symbol] 
        answer = calculation_function(last_answer, num2)
    
        # print the answer
        print(f"{last_answer} {operation_symbol} {num2} = {answer}")
    
        # Conditionals
        continue_calculating = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ")
        if continue_calculating == "n":
            clear()
            # Recursion
            calculator()
        elif continue_calculating == "y":
            # Save last answer
            last_answer = answer
        else:
            print("Error! Invalid option")
calculator()