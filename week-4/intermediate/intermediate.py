# Python shunting yard
#
# Input > 1 + 2 - 3
# Two arrays; operators (+, -, etc), and operands (1, 2, 3)
# Push 1 to operands stack

import re

operatorRegex = '[+, \-, *, /, (, )]+'
numRegex = '[0-9]+'

def getUserInput():
    print ("Please enter an equation:")
    userInput = input(" >>  ")

    return userInput

def calculate(userInput):
    string = userInput

    operands = re.findall(numRegex, string)
    operators = []

    # Iterate though userinput, push each operator to the stack
    for character in string:
        operatorChar = re.match(operatorRegex, character)
        if operatorChar != None:
            operators.append(character)

    print (operands)
    print (operators)

    return

def main():
    userInput = getUserInput()
    calculate(userInput)

    return

if __name__ == "__main__":
    main()