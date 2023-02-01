def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def lose():
    print("\nYOU LOSE!")
    print("Better luck next time!")
    exit(0)

def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i - 1]) != 1: #If difference between [i] and [i - 1] is not one  (i.e. same number or numbers with diffs > 1)
            return False
        i += 1
    return True

def start():
    xyz = []
    last = 0
    while True:
        print("Enter F to take the first chance.")
        print("Enter S to take the second chance.")
        chance = input("> ")
        if chance == "F":
            while True:
                if last == 20:
                    lose()
                else:
                    print("\nYour turn. ")
                    print("\nHow many numbers do you want to enter? ")
                    inp = int(input("> "))
                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print("Wrong input. You are disqualified from the game.")
                        lose()
                    i, j = 1, 1

                    print("Now enter the values: ")
                    while i <= inp:
                        a = int(input("> "))
                        xyz.append(a)
                        i += 1
                    last = xyz[-1]
                    if check(xyz) == True:
                        if last == 21:
                            lose()
                        else:
                            while j <= comp:
                                xyz.append(last + j)
                                j += 1
                            print("Order of inputs after the Computer's turn is: ", xyz)
                            last = xyz[-1]
                    else:
                        print("You did not print consecutive integers.")
                        lose()
        elif chance == "S":
            comp = 1
            last = 0
            while last < 20:
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j += 1
                print("Order of inputs after the Computer's turn is: ", xyz)
                print(xyz)
                if xyz[-1] == 20:
                    lose()

                else:
                    print("\nYour turn.")
                    print("\nHow many numbers do you want to enter? ")
                    inp = int(input("> "))
                    i = 1
                    print("Enter your values: ")
                    while i <= inp:
                        xyz.append(int(input("> ")))
                        i += 1
                    last = xyz[-1]
                    if check(xyz) == True:
                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        print("You did not print consecutive integers.")
                        lose()
            print("\nCONGRATULATIONS!")
            print("\nYou win!")
            exit(0)
        else:
            print("Wrong choice.")


game = True
while game == True:
    print("Player 2 is the computer.")
    print("Do you want to play the 21 game? Yes/No")
    ans = input("> ")
    if ans == "Yes":
        start()
    else:
        print("Do you want to quit the game? Yes/No")
        next = input("> ")
        if next == "Yes":
            print("Quitting the game...")
            exit(0)
        elif next == "No":
            print("Continuing...")
        else:
            print("Wrong choice.")