from flask import Flask, render_template, request, jsonify,Response
from Complaindb import *
from Donationsdb import *
from DashBoardEndpoints import *
import sqlite3


app = Flask(__name__, template_folder="Template/")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/complinform.html")
def Compli():
    return render_template("complinform.html")

@app.route("/complinform.html", methods=["POST"])
def Complainfrom():
  try:
    location = request.form.get("location")
    weight =int(request.form.get("weight"))
    contact = int(request.form.get("contact"))

    image = request.files.get("image")
    imgbin = image.read() if image else None

    dbUpload = AddCComplain(location,weight,contact,imgbin)
    if dbUpload:
      return jsonify({"message": "Complaint submitted successfully!"})
    else:
      return jsonify({"error": "Failed to upload to database."}), 500


  except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route("/donation.html")
def RenderDon():
  return render_template("donation.html")



@app.route("/donation.html", methods=["POST"])
def donate():
  try:
    Dname = request.form.get("name")
    Dmail =request.form.get("email")
    contact = int(request.form.get("phone"))
    dtype = request.form.get("donationType")
    description = request.form.get("description")
    pickup = request.form.get("pickup")

    dbUpload = AddDonation(Dname,Dmail,contact,dtype,description,pickup)

    if dbUpload:
      return jsonify({"message": "Complaint submitted successfully!"})
    else:
      return jsonify({"error": "Failed to upload to database."}), 500


  except Exception as e:
        return jsonify({"error": str(e)}), 500





@app.route('/dashb.html')
def dashb():
   return render_template('dashb.html')


@app.route('/DashBoard.html')
def dashboard():
    conn = sqlite3.connect("WasteManagement.db")
    conn.row_factory = sqlite3.Row
    csr = conn.cursor()
    complaints = csr.execute('SELECT Id,Location, ContactNumber, Weight, WasteImage FROM Complains').fetchall()
    donations = csr.execute('SELECT Id , Name, Email, ContactNumber, Dtype, DonationDescription, PickupDate FROM Donations').fetchall()
    conn.close()
    return render_template('DashBoard.html', complaints=complaints, donations=donations)

# DonotionsEndpoint
#
@app.route("/Dono")
def GetDono():
   return SendAllDetailsDonations()

# ComplainEndpoint
#

@app.route("/Comp")
def Getcomplain():
   return   SendAllDetailsComplainDb()



# image Endpoint
@app.route("/image/<int:id>")
def serve_image(id):
    img_blob = ImageParser(id)
    if img_blob:
        return Response(img_blob, mimetype="image/jpeg")
    return "Image not found", 404

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
