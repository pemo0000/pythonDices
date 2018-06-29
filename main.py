#!/usr/bin/python3
from Toss import *
import readchar

def startGame():
    toss.initial()
    while True:
        pressedKey = readchar.readkey()
        if pressedKey == 'N':
            print("New Game...\n")
            os.execv(sys.executable, ['python'] + sys.argv)
        elif pressedKey == 'E':
            exit(0)
        toss.roll()

toss = Toss()
startGame()
