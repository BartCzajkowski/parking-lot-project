"""
App created to keep track of parking lot spaces and cars which are occupying each spot
"""
import sqlite3
from sqlite3 import Error

#Functions

def Connection():
    '''Create a connection.Standard database is created in location of file'''
    global conn
    conn = None
    try:
        conn = sqlite3.connect("database.db")
    except Error as error:
        print(error)
    return conn

def ParkingCreation():
    '''Create a Parking lot.'''
    cur = conn.cursor()
    no_of_spaces = int(input("How many parking spaces are in a parking lot?: "))
    print(f'Okay, creating a parking lot with {no_of_spaces} spaces.')
    number_spaces = list(zip([item for item in range(1,(no_of_spaces + 1))]))

    cur.execute('''CREATE TABLE IF NOT EXISTS spaces (space_id int)''')

    cur.executemany('INSERT INTO spaces VALUES (?)', number_spaces)
    conn.commit()

def ListOfSpaces():
    '''Print number of parking spaces.'''
    cur = conn.cursor()
    cur.execute('SELECT * FROM spaces')
    data = cur.fetchall()
    print ("Here is a list of spaces:", data)
