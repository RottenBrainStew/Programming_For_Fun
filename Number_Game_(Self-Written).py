import random
print("Welcome to the number guessing game!")
lower = int(input(("Enter lower bound for random number: ")))
upper = int(input(("Enter upper bound for random number: ")))
randNum = random.randint(lower, upper)
guesses = (upper - lower) / 2
print("You have %d guesses to get the correct number. " % (guesses))
guess = int(input("Guess a number: "))
while (guess > 0):
    if (guess < randNum):
        print("Too low! Guess again.")
        guesses -= 1
        print("You have %d guesses left." % (guesses))
        guess = int(input("Guess again: "))
    elif (guess > randNum):
        print("Too high! Guess again.")
        guesses -= 1
        print("You have %d guesses left." % (guesses))
        guess = int(input("Guess again: "))
    elif (guess == randNum):
        print("You got the right number!")
        print("The random number is %d." % (randNum))
        break
    elif (guesses == 0):
        print("You lose!")
        print("The random number is %d." %(randNum))
        break
    else:
        print("Error. Please enter a valid number.")
        continue

