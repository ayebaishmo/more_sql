import sqlite3
import queries as qu
import pandas as pd
# # Coonection
# connection = sqlite3.connect('rpg_db.sqlite3')

# # make the cursor

# cursor = connection.cursor()

# # query
# query_1 = 'SELECT * FROM charactercreator_character;'

# results = cursor.execute(query_1).fetchall()

# if __name__=='__main__':
#     print(results[::5])

## The Above is going to be returned in to dry code i.e 
## we shalll be using function to avoid reptition

# connection to the database
# query_1 = 'SELECT * FROM charactercreator_character;'
# def connect_to_db(db_name = 'rpg_db.sqlite3'):
#     return sqlite3.connect(db_name)

# def execute_q(conn, query):
#     curs = conn.cursor()
#     curs.execute(query)
#     return curs.fetchall()

# if __name__ == '__main__':
#     conn =connect_to_db()
#     results = execute_q(conn, query_1)
#     print(results[::5])


# separating the query from the connnection
def connect_to_db(db_name = 'rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    return curs.fetchall()

if __name__ == '__main__':
    conn = connect_to_db()
    results = execute_q(conn, qu.TOTAL_ITEMS)
    # print(results[::5])

    # change the tuples to dataframes
    df = pd.DataFrame(results)
    print(df.head())

