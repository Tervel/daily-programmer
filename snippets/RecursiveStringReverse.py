def getUserInput():
    print ("Enter text to be reversed\n")
    userInput = input(" >>  ")

    return userInput

def reverseString(userInput):
    if len(userInput) <= 1:
        return userInput

    return reverseString(userInput[1:]) + userInput[0]

if __name__ == "__main__":
    userInput = getUserInput()
    text = reverseString(userInput)

    print ("The text reversed is: " + text)


