#!/usr/bin/python3
from Toss import *
import readchar

def startGame():
    toss.initial()
    while True:
        if readchar.readkey() == 'E':
            exit(0)
        toss.roll()
        # elif readchar.readkey() == 'N':
        #     os.execv(sys.executable, ['python'] + sys.argv)

toss = Toss()
startGame()