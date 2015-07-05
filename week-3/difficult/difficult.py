# Welcome to cipher day!
# For this challenge, you need to write a program that will take the 
# scrambled words from this post, and compare them against THIS WORD 
# LIST[1] to unscramble them. For bonus points, sort the words by length
#  when you are finished. Post your programs and/or subroutines!

# Here are your words to de-scramble:
# mkeart
# sleewa
# edcudls
# iragoge
# usrlsle
# nalraoci
# nsdeuto
# amrhat
# inknsy
# iferkna

from urllib.request import urlopen

# Local word list
# wordFile = open("wordlist.txt", "r")
# WORD_LIST = wordFile.read().split()
# wordFile.close()

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