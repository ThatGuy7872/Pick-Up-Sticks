import random
#Assigning amount of sticks
nSticks = 17

#Making function for best move
def move(nSticks):
    move1 = nSticks-1
    move2 = nSticks-2
    move3 = nSticks-3
    if move1 % 4 == 1:
        return 1
    elif move2 % 4 ==1:
        return 2
    elif move3 % 4 ==1:
        return 3
    else:
        return random.randint(1,3)

#Making function for player loss 
def lose():
    print ("The number of sticks is 0.")
    print ("You lose.")

#Taking input of player's name
sBlah = input("What is your name?")
sName = sBlah.title()

#Randomly choosing who goes first
def random():
    global randint
    nNumber = random.randint(1,2)
    if nNumber == 1:
        bPlayerfirst = True
        print(sName, "goes first.")
    else:
        bPlayerfirst = False
        print("The computer will go first")

#Game loop
def oneplayerhard():
    random()
    print("There are", nSticks, "sticks.")
    while nSticks > 0:
        if bPlayerfirst == True:
            nplayermove = int(input("How many sticks would you like to pick up? "))
            if nplayermove < 1:
                print("Incorrect input. Try again.")
            elif nplayermove >3:
                print("Incorrect input. Try again.")
            else:
                nSticks = nSticks - nplayermove
                if nSticks > 0:
                    print("There are",nSticks,"sticks.")
                    bPlayerfirst = False
                else:
                    lose1p()
                    break
        else:
            nAImove = move(nSticks)
            print("The computer takes",nAImove,"sticks.")
            nSticks = nSticks - nAImove
            if nSticks > 0:
                print("There are",nSticks,"sticks.")
                bPlayerfirst = True
            else:
                print("There are no sticks.")
                print("The computer loses.")
                break

oneplayerhard()

