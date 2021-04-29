import numpy as np


def diceRoll():
    die1 = np.random.randint(1,6)
    die2 = np.random.randint(1,6)
    die3 = np.random.randint(1,6)
    die4 = np.random.randint(1,6)
    return [die1, die2, die3, die4]
    