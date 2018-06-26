import sqlite3

def createDB():
    connection = sqlite3.connect("/tmp/pythonDices.db")
    cursor = connection.cursor()
    sql = "CREATE TABLE tosses(dice1,dice2)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Datenbank pythonDices.db angelegt.")