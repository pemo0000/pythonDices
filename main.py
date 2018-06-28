#!/usr/bin/python3
from __future__ import print_function
from dice import *
from db import *
import sys, readchar, os, sqlite3

if not os.path.exists("/tmp/pythonDices.db"):
    print("Datenbank pythonDices.db nicht vorhanden - Datenbank wird anglegt...")
    createDB()

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
        if numberRolls == 3 and (dice1.result == dice2.result):
            print("Pasch in initial toss. rolling again...")
            os.execv(sys.executable, ['python'] + sys.argv)
        connection = sqlite3.connect("/tmp/pythonDices.db")
        cursor = connection.cursor()
        sql = "INSERT INTO tosses VALUES(" + str(dice1.result) + "," + str(dice2.result) + ")"
        cursor.execute(sql)
        connection.commit()
        connection.close()
    else:
        print("\t", end='')
        print(str(dice1.roll()) + ' ', end='')
        dice1.speak()
        print(str(dice2.roll()) + ' ', end='')
        dice2.speak()
        print('')
        connection = sqlite3.connect("/tmp/pythonDices.db")
        cursor = connection.cursor()
        sql = "INSERT INTO tosses VALUES(" + str(dice1.result) + "," + str(dice2.result) + ")"
        cursor.execute(sql)
        connection.commit()
        connection.close()

    sys.stdout.flush()

    if readchar.readkey() == 'E':
        exit(0)
    # elif readchar.readkey() == 'N':
    #     os.execv(sys.executable, ['python'] + sys.argv)
