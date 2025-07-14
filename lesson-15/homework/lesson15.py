#1
import sqlite3
conn=sqlite3.connect('Sitora.db')
cursor=conn.cursor()
cursor.execute('''
            Create table Roster(
               Name text,
               species text,
               age int
               )
        ''')
conn.commit()
conn.close()
#2
import sqlite3
conn = sqlite3.connect('Sitora.db')
cursor = conn.cursor()
roster_data = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]

cursor.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?);', roster_data)
conn.commit()
conn.close()

#3
conn = sqlite3.connect('Sitora.db') 
cursor = conn.cursor()

cursor.execute('''
    UPDATE Roster
    SET Name = ?
    WHERE Name = ?
''', ('Ezri Dax', 'Jadzia Dax'))

conn.commit()
conn.close()

#4
conn = sqlite3.connect('Sitora.db') 
cursor = conn.cursor() 
cursor.execute('''
    SELECT Name, Age
    FROM Roster
    WHERE Species = ?
''', ('Bajoran',))

rows = cursor.fetchall()

for name, age in rows:
    print(f"Name: {name}, Age: {age}")

conn.close()
