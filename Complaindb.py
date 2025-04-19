"""
Schema for complain.db
CREATE TABLE IF NOT EXISTS  Complains(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Location TEXT NOT NULL,
        Weight INTEGER NOT NULL,
        ContactNumber INTEGER NOT NULL,
        WasteImage BlOB NOT NULL   ->convert Image binary and then store


"""

import sqlite3




def AddCComplain(loc:str|None , Wei:int|None , Contact:int|None , Wimg:bytes|None)->bool:
  try:
    conn =sqlite3.connect("WasteManagement.db")
    csr = conn.cursor()

    csr.execute('''
        CREATE TABLE IF NOT EXISTS Complains(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Location TEXT NOT NULL,
            Weight INTEGER NOT NULL,
            ContactNumber INTEGER NOT NULL,
            WasteImage BlOB NOT NULL
        )
    ''')
    csr.execute('''
      INSERT INTO Complains (Location, Weight, ContactNumber, WasteImage)
      VALUES (?, ?, ?, ?)''', (loc, Wei, Contact, Wimg))

    conn.commit()

    # testing db ->img is converted to hex for diplay purpose
    # csr.execute("SELECT * FROM Complains")
    # print(csr.fetchall())

    conn.commit()
    conn.close()
    return True
  except Exception as e:
    print("Database error:", e)
    return False
