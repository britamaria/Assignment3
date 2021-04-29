import numpy as np

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