import random
nSticks = 17

#Input names of players
sName1 = input("Input player 1 name: ")
sName2 = input("Input player 2 name: ")

#Randomly choosing who goes first
nNumber = random.randint(1,2)
if nNumber == 1:
    bPlayer1turn = True
    print(sName1, "will go first.")
else:
    bPlayer1turn = False
    print(sName2,"will go first")
#Function for loss
def lose2p(loser):
    print("The number of sticks is 0.")
    print(loser, "loses.")

#Game loop
print("There are", nSticks, "sticks.")
while nSticks > 0:
    if bPlayer1turn == True:
        print(sName1 + "'s turn.")
        nPlayermove = int(input("How many sticks would you like to pick up? "))
        if nPlayermove < 1:
            print("Incorrect input. Try again.")
        elif nPlayermove > 3:
            print("Incorrect input. Try again.")
        else:
            nSticks = nSticks - nPlayermove
            if nSticks > 0:
                print("There are", nSticks, "sticks.")
                bPlayer1turn = False
            else: lose2p(sName1)
    else:
        print(sName2 + "'s turn.")
        nPlayermove = int(input("How many sticks would you like to pick up? "))
        if nPlayermove < 1:
            print("Incorrect input. Try again.")
        elif nPlayermove > 3:
            print("Incorrect input. Try again.")
        else:
            nSticks = nSticks - nPlayermove
            if nSticks > 0:
                print("There are", nSticks, "sticks.")
                bPlayer1turn = True
            else: lose2p(sName2)
        
            
