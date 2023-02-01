import random
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
toGuess = random.randint(lower, upper)
guesses = (lower + upper) / 2
print("You have many %2d guesses to correctly guess the correct number.\n" % (guesses))
guess = int(input("Guess a number: "))
count = 0
while count < guesses:
    if guess > toGuess:
        print("Too high! Try again.")
        count += 1
        guess = int(input("Guess again: "))
    elif guess < toGuess:
        print("Too low! Try again.")
        count += 1
        guess = int(input("Guess again: "))
    elif guess == toGuess:
        print("That's correct!. You got the answer in %2d guesses!" % (count))
        break
    elif count == guesses:
        print("Sorry. You failed. The correct answer is %2d." % (toGuess))
        break

