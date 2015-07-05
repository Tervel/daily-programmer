# Your challenge for today is to create a program which is password protected,
# and wont open unless the correct user and password is given.
# For extra credit, have the user and password in a separate .txt file.
# for even more extra credit, break into your own program :)

from getpass import getpass

def checkPassword(userInput, userPassword):
    passwordValid = False
    userIndex = 0

    # Get users
    userFile = open("users.txt", "r")
    users = userFile.read().split("\n")
    userFile.close()

    # Get passwords
    passwordFile = open("passwords.txt", "r")
    passwords = passwordFile.read().split("\n")
    passwordFile.close()

    # Check if user is in list, store index
    for user in users:
        if user == userInput:
            userIndex = users.index(user)
            break

    # Check if the users password matches the input password
    if userPassword == passwords[userIndex]:
        passwordValid = True

    return passwordValid

def main():
    print("Enter username: ")
    userInput = input(" >>  ")

    print ("Enter password: ")
    userPassword = getpass(" >>  ")

    loggedIn = checkPassword(userInput, userPassword)

    if loggedIn:
        print ("Logged in!")
    else:
        print ("Incorrect password!")

    return

if __name__ == "__main__":
    main()