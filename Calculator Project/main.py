import operator

import art


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(art.logo)
    should_accumulate = True
    first_number = (int(input("What is your first number? ")))

    while should_accumulate:

       for symbol in dictionary:
          print(symbol)
       operation=(input("Pick an operation: "))
       second_number=int(input("What is your second number? "))
       answer = dictionary[operation](first_number, second_number)
       print(f"{first_number} {symbol} {second_number} = {answer}")
       choice = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.")

       if choice == "y":
            first_number = answer
       else:
           should_accumulate = False
           print("\n" * 20)
           calculator()


calculator()




