from urllib.request import urlopen

WORD_LIST = urlopen('http://pastebin.com/raw.php?i=jSD873gL').read().decode().split()

def main():
	matches = []
	scrambledWords = ['mkeart', 'sleewa', 'edcudls', 'iragoge', 'usrlsle',
					  'nalraoci', 'nsdeuto', 'amrhat', 'inknsy', 'iferkna']

	for scrambledWord in scrambledWords:
		for word in WORD_LIST:
			if sorted(scrambledWord) == sorted(word):
				matches.append(word)
				print (scrambledWord + ": " + word)

if __name__ == "__main__":
	main()