import random #random used to generate a random word
from collections import Counter
name = input("What is your name? ")
print("Good luck {}!".format(name))
wordFile = "words.txt"
words = open(wordFile).read().splitlines()
#print(words)
word = random.choice(words)
print(word)
for char in word:
    print('_', end = " ")
print()

playing = True
letterGuess = "" #Letters guessed by the player
chances = len(word) + 2
correct = 0 #Count the number of correct letters correctly guessed
flag = 0 #Will be one if the player wins by guessing all the letters

try:
    while chances != 0 and flag == 0:
        print()
        try:
            guess  = str(input("Enter a letter to guess: "))
        except:
            print("Enter a letter or a grammatical expression please!")
            continue
        if len(guess) > 1:
            print("Enter only a single letter please!")
            continue
        elif guess in letterGuess:
            print("You have already guessed that letter.")
            continue
        elif not guess.isalpha():
            print("Enter a letter or an apostrophe!")
            continue
        if guess in word:
            k = word.count(guess)
            for _ in range(k):
                letterGuess += guess
        for char in word:
            if char in letterGuess and (Counter(letterGuess) != Counter(word)):
                print(char, end = " ")
                correct += 1
                chances -= 1
            elif (Counter(letterGuess) == Counter(word)):
                print("The word is {}.".format(word))
                flag = 1
                print("Congratulations. You win!")
                break
                break
            else:
                print('_', end = " ")
    if chances == 0 and (Counter(letterGuess) == Counter(word)):
        print()
        print("You lost!")
        print("The word was {}.".format(word))

except KeyboardInterrupt:
    print()
    print('Bye! Try again.')
    exit()
