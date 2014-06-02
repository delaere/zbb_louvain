import sys

file = sys.argv[1]
wordToReplace = sys.argv[2]
newWord = sys.argv[3]

fCard = open(file, "r")
temp = fCard.read()
fCard.close()
temp = temp.replace(wordToReplace, newWord)
fCard = open(file, "w")
fCard.write(temp)
fCard.close()
