

import sqlite3
from flask import jsonify,url_for



def SendAllDetailsDonations():
  try:
    conn =sqlite3.connect("WasteManagement.db")
    conn.row_factory = sqlite3.Row
    csr = conn.cursor()
    dono = csr.execute('SELECT Id, Name, Email, ContactNumber,Dtype,DonationDescription, PickupDate FROM Donations').fetchall()
    conn.close()
    return jsonify([dict(row) for row in dono])

  except Exception as e:
    return jsonify({"error": str(e)}), 500

def SendAllDetailsComplainDb():
    try:
        conn = sqlite3.connect("WasteManagement.db")
        conn.row_factory = sqlite3.Row
        csr = conn.cursor()
        complaints = csr.execute('SELECT Id, Location, Weight, ContactNumber FROM Complains').fetchall()
        conn.close()

        # Convert rows to dict and add image URL
        complaint_list = []
        for row in complaints:
            row_dict = dict(row)
            row_dict["ImageURL"] = url_for('serve_image', id=row["Id"])
            complaint_list.append(row_dict)

        return jsonify(complaint_list)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def ImageParser(Id:int|None):
  try:
    conn =sqlite3.connect("WasteManagement.db")
    csr = conn.cursor()
    csr.execute("SELECT WasteImage FROM Complains WHERE Id = ?", (Id,))
    imgblob=csr.fetchone()
    conn.close()
    if imgblob and imgblob[0]:
      return imgblob[0]
    else:
      return None
  except Exception as e:
    return str(e)
