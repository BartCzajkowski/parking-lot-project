"""
App created to keep track of parking lot spaces and cars which are occupying each spot
"""
import sqlite3

#Establishing number of spaces in a  parking lot
no_of_spaces = int(input("How many parking spaces are in a parking lot?: "))
print(f'Okay, creating a parking lot with {no_of_spaces} spaces.')
number_spaces = list(zip([item for item in range(1,(no_of_spaces + 1))]))

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS spaces
            (space_id int)''')

cur.executemany('INSERT INTO spaces VALUES (?)', number_spaces)
conn.commit()

cur.execute('SELECT * FROM spaces')
data = cur.fetchall()
print ("Here is a list of spaces:", data)
