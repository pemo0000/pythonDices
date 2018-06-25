from dice import *

dice1 = dice()
dice2 = dice()
numberRolls = 0

while True:
    print(str(dice1.roll()) + ' ', end='')
    dice1.speak()
    print(dice2.roll())
    dice2.speak()
    input()
    numberRolls += 1
    print(numberRolls)
