import sqlite3

#creates connection 
conn = sqlite3.connect('test_database.db')

#creating table 
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    cur.execute("INSERT INTO People VALUES('Ron', 'Stoppable', 16)")
    conn.commit()



