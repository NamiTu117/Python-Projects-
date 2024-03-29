import sqlite3


#making the database
conn = sqlite3.connect('scrpt.db')
#fetching files from the current working directory



#creating tables
with conn:
    cur = conn.cursor()
    cur.execute ("CREATE TABLE IF NOT EXISTS tbl_assignment ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name TEXT)")
    conn.commit()

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg','World.txt', 'data.pdf', 'myPhoto.jpg')


conn = sqlite3.connect('scrpt.db')
with conn:
    #checking for files 
     for file in fileList: 
        #checking files with txt extension
        if file.endswith(".txt"):
            with conn:
                cur=conn.cursor()
            #prints names of txt files
            cur.execute("INSERT INTO tbl_assignment (col_name) VALUES(?)",(file,))
            print(file)
        conn.commit()
