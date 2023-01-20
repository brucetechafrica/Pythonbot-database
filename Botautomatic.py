import psycopg2

# Connect to the first database
conn1 = psycopg2.connect(dbname='database1', user='user1', password='password1', host='localhost')
cursor1 = conn1.cursor()

# Connect to the second database
conn2 = psycopg2.connect(dbname='database2', user='user2', password='password2', host='localhost')
cursor2 = conn2.cursor()

# Query both databases to retrieve the necessary information
cursor1.execute('SELECT * FROM table1')
results1 = cursor1.fetchall()
cursor2.execute('SELECT * FROM table2')
results2 = cursor2.fetchall()

# Iterate through the results, comparing the data from each row
for row1, row2 in zip(results1, results2):
    if row1 != row2:
        print('Discrepancy found:', row1, row2)

# Close the cursors and connections
cursor1.close()
cursor2.close()
conn1.close()
conn2.close()
