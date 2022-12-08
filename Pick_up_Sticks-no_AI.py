import random
nsticks = 17
print("The number of sticks is",nsticks)


while nsticks > 0:
    move = int(input("Enter your number: "))
    if move < 1:
        print("Incorrect input. Try again. ")
        continue
    elif move > 3:
        print("Incorrect input. Try again. ")
        continue
    else:
        nsticks = nsticks - move
        if nsticks > 0:
            print("There are",nsticks,"sticks")
        else:
            print("There are no sticks")
        continue
print("You lose")
