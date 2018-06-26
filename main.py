#!/usr/bin/python3
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