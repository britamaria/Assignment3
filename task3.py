import numpy as np
import matplotlib.pyplot as plt 
import diceRoll as dr
import judger as jg



options=["Player1: Roll the dice", "Player2: Roll the dice"]

def diceRoll():
    #randomIndex= np.random.randint(0,3)
    die1 = np.random.randint(1,6)
    die2 = np.random.randint(1,6)
    die3 = np.random.randint(1,6)
    die4 = np.random.randint(1,6)
    #return options[randomIndex] 
    if die1 == die2 or die1 + die2 > die3 + die4:

        print("Player one wins!")

    print(die3, die4)
    print(die3 + die4)

    if die3 == die4 or die1 + die2 < die3 + die4:
    
        print("Player two wins!")
    
    
    if die1 == die2 or die3 == die4 or die1 + die2 == die3 + die4:
    
        print("Stalemate! Roll gain.")
    #return diceRoll()

player1 = diceRoll()
player2 = diceRoll()

# print("player1:", player1)
# print("player2:", player2)

# def judger(opt1,opt2): 
# #   utelukke feil input og uavgjort
#     if opt1 not in options or opt2 not in options:
#         return -1
# #   uavgjot
#     if opt1 == opt2:
#         return 0
    
#     index1 = options.index(opt1)
#     index2 = options.index(opt2)
    
#     if(index1 + 1 == index2):
#         return 2
# #   len(options -1 vil være lik 2, eller den siste indexen)
#     elif(index1==len(options)-1 and index2== 0):
#         return 2
#     else: 
#         return 1
    
def Judger(dices):
    p1 = 0 
    p2 = 1
    draw = 2
    player1 = [dices[0], dices[1]]
    player2 = [dices[2], dices[3]]
    
    if(player1[0] == player1[1] and player2[0] == player2[1]):
        if(player1[0] == player2[0]):
            return draw
        elif(player1[0] > player2[0]):
            return p1
        else:
            return p2
    elif(player1[0] == player1[1]):
        return p1
    elif(player2[0] == player2[1]):
        return p2
    elif(np.sum(player1) == np.sum(player2)):
        return draw
    elif(np.sum(player1) > np.sum(player2)):
        return p1
    else:
        return p2 
    
    
Player1 = diceRoll()
Player2 = diceRoll()
result = Judger(player1, player2)
print(player1,player2,result)

def simulateGame(nGames):
    p1 = 0
    p2 = 0
    tie = 0
    
    for i in range(nGames):
        roll1 = diceRoll()
        roll2 = diceRoll()
        print("player 1 rolls")
        print("player 2 rolls")
        result = Judger(roll1,roll2)
        if(result == -1):
            print("Wrong input")
        elif(result == 0):
            print("Tie")
            tie += 1
        elif(result == 1):
            print("player 1 wins")
            p1 += 1
        elif(result == 2):
            print("player 1 wins")
            p1 += 2
    print("final score: ")
    print("    player 1:", p1)
    print("    player 2:", p2)
    print("    Tie:", tie)
    
    return p1,p2,tie

a = simulateGame(1)
print(a)