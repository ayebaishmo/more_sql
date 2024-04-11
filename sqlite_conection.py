import sqlite3


# Coonection
connection = sqlite3.connect('rpg_db.sqlite3')

# make the cursor

cursor = connection.cursor()

# query
query_1 = 'SELECT * FROM charactercreator_character;'

results = cursor.execute(query_1).fetchall()

if __name__=='__main__':
    print(results[::5])
