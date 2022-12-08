import random
nSticks = 17

#Input names of players
sName1 = input("Input player 1 name: ")
sName2 = input("Input player 2 name: ")
sName1 = sName1.title()
sName2 = sName2.title()

#Randomly choosing who goes first
nNumber = random.randint(1,2)
if nNumber == 1:
    bPlayer1turn = 1
    print(sName1, "will go first.")
else:
    bPlayer1turn = 2
    print(sName2,"will go first")
#Function for loss
def lose2p(loser):
    print(loser, "loses.")

#Game loop
while nSticks > 0:
    if bPlayer1turn % 2 == 1:
        print(sName1 + "'s turn.")
    else:
        print(sName2 + "'s turn.")
    print("There are", nSticks, "sticks left.")
    nPlayermove =input("How many sticks would you like to pick up? ")
    while nPlayermove.isnumeric() == False:
        print("Incorrect input. Try again.")
        nPlayermove = input("Input your number: ")
    nPlayermove = int(nPlayermove)
    if nPlayermove < 1 or nPlayermove > 3:
         print("Incorrect input. Try again.")
    else:
        nSticks = nSticks - nPlayermove
        if nSticks <= 0:
            print("There are no sticks.")
            if bPlayer1turn % 2 == 1:
                lose2p(sName1)
            else:
                lose2p(sName2)
        bPlayer1turn = bPlayer1turn + 1
