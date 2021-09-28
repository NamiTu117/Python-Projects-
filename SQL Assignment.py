import sqlite3

conn = sqlite3.connect('test_database.db')

with conn:
    cur.execute("INSERT INTO People VALUES('Ron', 'Stoppable', 16)")
    conn.commit()
    
    


