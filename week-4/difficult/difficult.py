# today, your challenge is to create a program that will take a series 
# of numbers (5, 3, 15), and find how those numbers can 
# add, subtract, multiply, or divide in various ways to relate to eachother. 
# This string of numbers should result in 5 * 3 = 15, or 15 /3 = 5, or 15/5 = 3. 
# When you are done, test your numbers with the following strings:
# 4, 2, 8
# 6, 2, 12
# 6, 2, 3
# 9, 12, 108
# 4, 16, 64
# For extra credit, have the program list all possible combinations.
# for even more extra credit, allow the program to deal with strings of 
# greater than three numbers. For example, an input of (3, 5, 5, 3) would 
# be 3 * 5 = 15, 15/5 = 3. When you are finished, test them with the 
# following strings.
# 2, 4, 6, 3
# 1, 1, 2, 3
# 4, 4, 3, 4
# 8, 4, 3, 6
# 9, 3, 1, 7

import itertools
import re

numRegex = '[0-9]+'
operators = {
    "+" : lambda a, b: a + b,
    "*" : lambda a, b: a * b,
    "-" : lambda a, b: a - b,
    "/" : lambda a, b: a / b,
    "%" : lambda a, b: a % b,
}

def getInput():
    print("Enter three separate numbers, eg; 1, 2, 3: ")
    userinput = input(" >>  ")

    return userinput

def applyOperator(operation, valueOne, valueTwo):
    return operators[operation](valueOne, valueTwo)

def main():
    results = []

    userinput = getInput()
    numbers = re.findall(numRegex, userinput)
    inputPermutations = list(itertools.permutations([numbers[0], numbers[1], numbers[2]]))

    # for each operator, iterate through all combinations of x, y, z
    # eg: 1, 2, 3 > 1 + 2 = 3
    #               3 - 2 = 1
    #               ..... = ...
    # if x, y = z then print the operation + combination
    for operation in operators:
        for permutation in inputPermutations:
            result = applyOperator(operation, int(permutation[0]), int(permutation[1]))
            if float(permutation[2]) == float(result):
                print ("{0} {1} {2} = {3}".format(permutation[0], operation, permutation[1], result))

    return

if __name__ == "__main__":
    main()