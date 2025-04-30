"""
Schema for Donations.db
CREATE TABLE IF NOT EXISTS  Donations(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Email TEXT NOT NULL,
        Password TEXT NOT NULL
"""

import sqlite3





def AddUser( Email:str|None , Password:str|None )->bool:
  try:
    conn =sqlite3.connect("UserLogin.db")
    csr = conn.cursor()

    csr.execute('''
      CREATE TABLE IF NOT EXISTS  Users(
              Id INTEGER PRIMARY KEY AUTOINCREMENT,
              Email TEXT NOT NULL,
              Password TEXT NOT NULL
        )
    ''')
    csr.execute('''
            INSERT INTO  Users(Email,Password )
            VALUES (?, ?)
        ''', (Email, Password))
    conn.commit()


    # # testing db ->
    # csr.execute("SELECT * FROM Users")
    # print(csr.fetchall())
    # conn.commit()


    conn.close()
    return True
  except Exception as e:
    print("Database error:", e)
    return False



import sqlite3

def Check_user(email: str | None, password: str | None) -> bool:
    try:
        conn = sqlite3.connect("UserLogin.db")
        csr = conn.cursor()

        # # Ensure table exists
        # csr.execute('''
        #     CREATE TABLE IF NOT EXISTS Users(
        #         Id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         Email TEXT NOT NULL,
        #         Password TEXT NOT NULL
        #     )
        # ''')

        # # Query to check if user exists
        csr.execute('''
            SELECT * FROM Users WHERE Email = ? AND Password = ?
        ''', (email, password))

        result = csr.fetchone()

        conn.close()

        # If a match is found, return True
        return result is not None

    except Exception as e:
        print("Database error:", e)
        return False
