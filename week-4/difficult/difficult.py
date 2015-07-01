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