import sqlite3

conn = sqlite3.connect('MeteoriteData.sqlite')
cur = conn.cursor()

cur.execute('SELECT NASA_id, latitude, longitude, state, country FROM Location WHERE state is null ORDER BY NASA_id LIMIT 2')

try:
    row = cur.fetchone()
    print(row[0],row[1],row[2])
except:
    print('failed')

# for row in cur :
#     #data = str(row[1].decode())
#     try:
#         print(row[0],row[1],row[2], row[3])
#     except:
#         continue


cur.close()
