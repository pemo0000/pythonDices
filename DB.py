import sqlite3
import os

class DB:

    def __init__(self):
        self.createDB()
        self.connection = sqlite3.connect("pythonDices.db")
        self.cursor = self.connection.cursor()

    def createDB(self):
        if not os.path.exists("pythonDices.db"):
            print("Datenbank pythonDices.db nicht vorhanden - Datenbank wird anglegt...")
            self.connection = sqlite3.connect("pythonDices.db")
            self.cursor = self.connection.cursor()
            sql = "CREATE TABLE tosses(dice1,dice2)"
            self.cursor.execute(sql)
            print("Datenbank pythonDices.db angelegt.")

    def insertToss(self, dice1, dice2):
        sql = "INSERT INTO tosses VALUES(" + str(dice1) + "," + str(dice2) + ")"
        self.cursor.execute(sql)

    def __del__(self):
        self.connection.commit()
        self.connection.close()