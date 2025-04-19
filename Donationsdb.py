"""
Schema for Donations.db
CREATE TABLE IF NOT EXISTS  Donations(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        DonarEmail TEXT NOT NULL,
        ContactNumber INTEGER NOT NULL,
        Dtype TEXT NOT NULL,
        DonationDescription TEXT ,
        PickupDate TEXT NOT NULL
"""

import sqlite3





def AddDonation( Name:str|None , Email:str|None , Contact:int|None ,  Dtype:str|None , DonDesc:str|None , Pdate:str|None )->bool:
  try:
    conn =sqlite3.connect("WasteManagement.db")
    csr = conn.cursor()

    csr.execute('''
      CREATE TABLE IF NOT EXISTS  Donations(
              Id INTEGER PRIMARY KEY AUTOINCREMENT,
              Name TEXT NOT NULL,
              Email TEXT NOT NULL,
              ContactNumber INTEGER NOT NULL,
              Dtype TEXT NOT NULL,
              DonationDescription TEXT ,
              PickupDate TEXT NOT NULL
        )
    ''')
    csr.execute('''
            INSERT INTO Donations (Name, Email, ContactNumber, Dtype, DonationDescription, PickupDate)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (Name, Email, Contact, Dtype, DonDesc,Pdate))
    conn.commit()


    # testing db ->
    # csr.execute("SELECT * FROM Donations")
    # print(csr.fetchall())
    # conn.commit()


    conn.close()
    return True
  except Exception as e:
    print("Database error:", e)
    return False
