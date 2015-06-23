import random

def getUserInput():
    print ("Hello, please enter the length of the password you wish to be generated:")
    userInput = input(" >>  ")

    return int(userInput)

def generatePassword(userInput):
    passwordLength = userInput
    password = ""

    # Generate our password with given length
    for i in range(0, passwordLength):
        # Modulo by 93 + 33 to produce the range of ASCII characters we want for the password
        password += chr(random.getrandbits(56) % 93 + 33)

    return password

def main():
    userInput = getUserInput()
    generatedPassword = generatePassword(userInput)

    print (generatedPassword)
    return

if __name__ == "__main__":
    main()

