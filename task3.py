import numpy as np
import matplotlib.pyplot as plt 
import diceRoll as dr
import judger as jg



options=["Player1: Roll the dice", "Player2: Roll the dice"]



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