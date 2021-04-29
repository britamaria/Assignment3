from diceRoll import Roll
from judger import judge



options=["Player1: Roll the dice", "Player2: Roll the dice"]


  
player1 = Roll()
player2 = judge()
result = judge(player1, player2)
print(player1,player2,result)

def simulateGame(nGames):
    p1 = 0
    p2 = 0
    tie = 0
    
    for i in range(nGames):
        roll1 = Roll()
        roll2 = Roll()
        print("player 1 rolls")
        print("player 2 rolls")
        result = judge(roll1,roll2)
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



