#!/usr/bin/python3
from dice import *
import sys
import readchar

dice1 = dice()
dice2 = dice()
numberRolls = 2

while True:
    numberRolls += 1
    if numberRolls & 1:
        print(str(numberRolls >> 1) + '\t', end='')
        print(str(dice1.roll()) + ' ', end='')
        dice1.speak()
        print(str(dice2.roll()) + ' ', end='')
        dice2.speak()
    else:
        print ("\t", end='')
        print(str(dice1.roll()) + ' ', end='')
        dice1.speak()
        print(str(dice2.roll()) + ' ', end='')
        dice2.speak()
        print('')

    sys.stdout.flush()
    readchar.readkey()
