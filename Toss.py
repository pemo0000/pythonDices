from __future__ import print_function
import sys
from Dice import *
from DB import *

class Toss:

    def __init__(self):
        self.db = DB()
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.number = 0

    def roll(self):
        self.dice1.roll()
        self.dice2.roll()
        self.db.insertToss(self.dice1.result, self.dice2.result)
        if self.number or not self.isPasch():
            self.number += 1
        self.print()

    def isPasch(self):
        return self.dice1.result == self.dice2.result

    def print(self):
        if not self.number:
            print(str(self.dice1.result) + ',' + str(self.dice2.result))
        elif self.number & 1:
            print(str((self.number+2) >>1) + '\t', end='')
            print(str(self.dice1.result) + ' ', end='')
            self.dice1.speak()
            print(str(self.dice2.result) + ' ', end='')
            self.dice2.speak()
        else:
            print("\t", end='')
            print(str(self.dice1.result) + ' ', end='')
            self.dice1.speak()
            print(str(self.dice2.result) + ' ', end='')
            self.dice2.speak()
            print('')

        sys.stdout.flush()

    def initial(self):
        while True:
            self.roll()
            if not self.isPasch():
                self.number = 1
                return
            else:
                self.number = 0
