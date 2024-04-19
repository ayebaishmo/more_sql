import numpy as np
import pandas as pd
import sqlite3 as sq
data = 'C:/Users/ISHMO_CT/Downloads/Bloomtech/more_sql/buddymove_holidayiq.csv'
df = pd.read_csv(data)
print(df.head())

conn = sq.connect('buddymove_holidayiq.sqlite3')

df.to_sql('review', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

rows = '''SELECT 
    COUNT(*)
    FROM review'''

nature_shooping = '''
    SELECT COUNT(*) AS num_users
    FROM review
    WHERE Nature >= 100 AND Shopping >= 100;
    '''

avg_cat = '''
    SELECT 
        AVG(Sports) AS avg_sports,
        AVG(Religious) AS avg_religious,
        AVG(Nature) AS avg_nature,
        AVG(Theatre) AS avg_theatre,
        AVG(Shopping) AS avg_shopping,
        AVG(Picnic) AS avg_picnic
    FROM review;'''


