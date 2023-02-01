import random

name = input("What is your name? ")
print("Good luck {}!".format(name))
wordFile = "words.txt" #Import a file from Github with this name to choose random words
#Note: words.txt has to be in the same directory as python script, words.txt is /usrs/share/dict/words from Github
words = open(wordFile).read().splitlines()
guessNum = 10
gN = 10 #Placeholder number with the same value as guessNum to figure out how many guesses someone needed to get the correct word
wordList = words
print("You will have %d guesses to get the word correct." % (guessNum))
guessWord = random.choice(wordList)
count = 0
guesses = ""
print(guessWord)

while guessNum > 0:
    failed = 0
    for char in guessWord:
        if char in guesses:
            print(char, end = " ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You win!")
        print("The word is {}! You got the correct word in {} guesses!".format(guessWord, gN - guessNum))
        break
    print()
    guess = input("Guess a character: ")
    guesses += guess
    if guess not in guessWord:
        guessNum -= 1
        print("Wrong.")
        print("You have %d more turns left." % guessNum)
        if guessNum == 0:
            print("You lose. The correct word is {}".format(guessWord))