"""
App created to keep track of parking lot spaces and cars which are occupying each spot
"""
import sqlite3
from sqlite3 import Error

#Functions

conn = sqlite3.connect("database.db")
def cursor():
    return sqlite3.connect("database.db").cursor()

def parking_creation():
    '''Create a parking lot.'''
    cur = cursor()
    no_of_spaces = int(input("How many parking spaces are in a parking lot?: "))

    print(f'Okay, creating a parking lot with {no_of_spaces} spaces.')
    number_spaces = list(zip([item for item in range(1,(no_of_spaces + 1))]))
    with cur.connection:
        cur.execute('''CREATE TABLE IF NOT EXISTS spaces (space_id int UNIQUE, car_plate text)''')

        cur.executemany('INSERT OR REPLACE INTO spaces (space_id) VALUES (?)', number_spaces)
    cur.connection.close()

def parking_deletion():
    '''Delete current parking lot'''
    cur = cursor()
    cur.execute('DROP TABLE IF EXISTS spaces')
    conn.commit()
    cur.connection.close()

def spaces_list():
    '''Print number of parking spaces.'''
    cur = cursor()
    cur.execute('SELECT * FROM spaces')
    data = cur.fetchall()
    print ("Here is a list of spaces:\n(Space number, Car plate number)")
    for n in range (len(data)):
        print(data[n])
    cur.connection.close()

def spaces_assign():
    '''Assign a car plate number into a selected space'''
    cur = cursor()
    space_number = int(input('Which space would you like to assign?: '))
    plate_number = str.upper(input('Please specify plate number: '))
    cur.execute('SELECT * FROM spaces WHERE space_id=?', (space_number,))
    old_plate_number = cur.fetchone()
    print(old_plate_number, "Is now being assigned to: ")

    with cur.connection:
        cur.execute('UPDATE spaces SET car_plate=? WHERE space_id=?',
        (plate_number, space_number,))
    conn.commit()
    cur.execute('SELECT * FROM spaces WHERE space_id=?', (space_number,))
    space= cur.fetchone()
    print(space)
    cur.connection.close()

def spaces_delete():
    '''Delete a specific space (eg. obstructed space, damage to a space'''
    cur = cursor()
    space_number = int(input('Which space would you like to delete?: '))
    with cur.connection:
        cur.execute('DELETE FROM spaces WHERE space_id=?', (space_number,))
    cur.connection.close()

def spaces_create():
    '''Create a new space, must not be with used number'''
    space_number = [int(input('Adding space, please specify the number of space: '))]
    cur = cursor()
    with cur.connection:
        cur.execute('INSERT OR ABORT INTO spaces (space_id) VALUES (?)', (space_number))
    cur.connection.close()
