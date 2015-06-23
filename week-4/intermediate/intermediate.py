# Python shunting yard
#
# Input > 1 + 2 - 3
# Two arrays; operators (+, -, etc), and operands (1, 2, 3)
# Push 1 to operands stack

import re

operations = {
    "+" : lambda a, b: a + b,
    "*" : lambda a, b: a * b,
    "-" : lambda a, b: a - b,
    "/" : lambda a, b: a / b,
}

operatorRegex = '[+, \-, *, /]+'
separatorRegex = '[(, )]+'
numRegex = '[0-9]+'

def precedence(operator):
    return {
        '^': 4,
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
    }.get(operator, 'Error') # Default

def getUserInput():
    print ("Please enter an equation:")
    userInput = input(" >>  ")

    return userInput

def calculate(userInput):
    string = userInput

    operands = re.findall(numRegex, string)
    operators = []
    tokenList = []

    output = []
    stack = []

    # Tokenize input
    for character in string:
        operatorChar = re.match(operatorRegex, character)
        if operatorChar != None:
            operators.append(character)

    # Shunting yard
    tokenList = operands + operators
    for token in tokenList: # read a token
        numberToken = re.match(numRegex, token)
        operatorToken = re.match(operatorRegex, token)

        if numberToken != None: # if token is a number, add to output
            output.append(token)
        elif operatorToken != None: # if token is an operator
            o1 = token
            while len(stack) and precedence(o1) <= precedence(stack[-1]): # while there are operators in stack
                output.append(stack.pop()) # pop top of stack, and push to output
            stack.append(o1) # push o1 onto stack
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while not len(stack) and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop() # pop '(' from stack

    while len(stack): # while stack not empty
        output.append(stack.pop())

    print (output)
    print (stack)

    return

def main():
    userInput = getUserInput()
    calculate(userInput)

    return

if __name__ == "__main__":
    main()