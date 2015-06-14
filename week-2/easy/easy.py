import sys, os


def mainMenu():
	print "Choose an option:"
	print "1. Calculate force"
	print "2. Calculate mass"
	print "3. Calculate acceleration\n"
	choice = raw_input(" >>  ")
	menuChoice(choice)

	return

def menuChoice(choice):
	choice = choice.lower()

	if choice == '':
		mainMenu()
	else:
		try:
			menuActions[choice]()
		except KeyError:
			print "Invalid selection!\n"
			mainMenu()

	return

def calcForce():
	mass = float(raw_input("Enter Mass: "))
	acceleration = float(raw_input("Enter Acceleration: "))
	force = mass * acceleration

	print "\nForce: %d\n" % force

	mainMenu()
	return 


def calcMass():
	force = float(raw_input("Enter Force: "))
	acceleration = float(raw_input("Enter Acceleration: "))
	mass = force / acceleration

	print "\nMass: %d\n" % mass

	mainMenu()
	return  

def calcAcceleration():
	force = float(raw_input("Enter Force: "))
	mass = float(raw_input("Enter Mass: "))
	acceleration = force / mass

	print "\nAcceleration: %d\n" % acceleration

	mainMenu()
	return 

# Menu actions
menuActions = {
    '1': calcForce,
    '2': calcMass,
    '3': calcAcceleration,
}

if __name__ == "__main__":
	mainMenu()