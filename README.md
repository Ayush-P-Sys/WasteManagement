
# 🗑️ Waste Management Web App

This is a lightweight Flask-based web application to submit complaints and donation requests related to waste management and view them on a dashboard.

---

## 🚀 Features

- Submit waste complaints with images
- Record donation information
- Dashboard to view all records
- Endpoints to serve data via JSON
- Image viewing from the database

---

## 🧰 Requirements

- Python 3.8 or above
- Flask

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/waste-management-app.git
cd waste-management-app
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the App

```bash
python App.py
```

Navigate to: `http://localhost:5000` to use the app.

---

## 📁 Folder Structure

```
├── App.py
├── Complaindb.py
├── Donationsdb.py
├── DashBoardEndpoints.py
├── requirements.txt
├── Template/
│   ├── index.html
│   ├── complainform.html
│   ├── donation.html
│   └── DashBoard.html
```

---

## 📦 API Endpoints

| Endpoint       | Description                         |
|----------------|-------------------------------------|
| `/Comp`        | Returns all complaints as JSON      |
| `/Dono`        | Returns all donations as JSON       |
| `/image/<id>`  | Serves image of a specific complaint|

---

## 📌 Notes

- All data is stored in `WasteManagement.db`.
- Images are stored as binary (BLOB) in SQLite.
- Make sure the `Template/` folder exists and contains the HTML files.

---

## 🧑‍💻 Contributing

Feel free to fork and contribute via pull requests!

---

## 📄 License

This project is open-sourced under the MIT License.
