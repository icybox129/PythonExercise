from dice import diceRoll

#define function
def doubledice():
    #roll 1 dice set as vaiable
    dice1 = diceRoll()
 
    #roll 2nd dice set as variable
    dice2 = diceRoll()
    return f"Dice 1: {dice1}\nDice 2: {dice2}\nTotal: {dice1+dice2}"
    #return both added up

print(doubledice())