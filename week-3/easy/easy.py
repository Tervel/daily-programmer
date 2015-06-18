def getUserInput():
	print ("Enter text to be rotated\n")
	userInput = input(" >>  ")

	return userInput

def getRot():
	print ("Enter by how much\n")
	userInput = input(" >>  ")

	return int(userInput)

def rotN(userInput, n):
	wordList = list(userInput)
	rotatedWordList = []
	for word in wordList:
		value = ord(word)

		# If word isn't a capital letter
		if value >= ord('a') and value <= ord('z'):
			rotatedWord = chr(ord('a') + (value - ord('a') + n) % 26)
		elif value >= ord('A') and value <= ord('Z'): # Otherwise, if it is a capital letter
			rotatedWord = chr(ord('A') + (value - ord('a') + n) % 26)

		rotatedWordList.append(rotatedWord)

	rotatedWordList = ''.join(rotatedWordList)

	return rotatedWordList

def main():
	userInput = getUserInput()
	rotAmount = getRot()
	rotatedInput = rotN(userInput, rotAmount)
	
	print(rotatedInput)
	return

if __name__ == "__main__":
	main()

	